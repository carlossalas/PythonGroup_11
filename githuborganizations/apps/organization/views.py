from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views import View
from django.urls import reverse
import requests

from githuborganizations.views import Main
from apps.organization.forms import SearchForm
from apps.organization.models import Organizations
from apps.repository.models import Repositories
from apps.member.models import Members


class Organization(Main, View):
    def get(self, request):
        errors = []
        organization_login = ''
        organization_data = False

        if 'organization' in request.GET:
            organization_login = request.GET['organization']

            try:
                organization_data = Organizations.objects.get(login=organization_login)
            except Organizations.DoesNotExist:
                request_organization = requests.get('https://api.github.com/orgs/' + organization_login, auth=self.auth)
                if request_organization.status_code == 200:
                    organization_data = request_organization.json()
                else:
                    errors.append('No se encontro la organizacion enviada')

        return render(request, 'organization/search.html', {
            'form': SearchForm({'organization': organization_login}),
            'organization': organization_data,
            'errors': errors
        })


class Import(Main, View):
    repositories = []

    def get(self, request, organization_login=False):

        try:
            organization = Organizations.objects.get(login=organization_login)
            return HttpResponseRedirect(reverse('repository:index', args=[organization_login]))
        except Organizations.DoesNotExist:
            # Obtener Datos de Organización
            organization_request_url = 'https://api.github.com/orgs/' + organization_login
            organization_request = requests.get(url=organization_request_url, auth=self.auth)
            organization = organization_request.json()

            # Guardar Organización
            organization = self.saveOrganization(organization)

            # Guardar Repositorios
            self.saveRepositories(organization)

            # Guardar Miembros
            self.saveMembers(organization)

            return HttpResponseRedirect(reverse('repository:index', args=[organization.login]))

    @staticmethod
    def saveOrganization(organization):
        return Organizations.objects.create(
            login=organization['login'],
            name=organization['name'],
            description=organization['description'],
            avatar_url=organization['avatar_url'],
            blog=organization['blog'],
            email=organization['email'],
            public_repos=organization['public_repos'],
        )

    def saveRepositories(self, organization):
        if organization.public_repos > 0:
            self.getAllRepositories('https://api.github.com/orgs/' + organization.login + '/repos?type=public')
            repositoriesObjects = []
            for repository in self.repositories:
                repositoriesObjects.append(Repositories(
                    name=repository['name'],
                    html_url=repository['html_url'],
                    description=repository['description'],
                    language=repository['language'],
                    stargazers_count=repository['stargazers_count'],
                    forks_count=repository['forks_count'],
                    created_at=repository['created_at'],
                    updated_at=repository['updated_at'],
                    organization=organization,
                ))
            Repositories.objects.bulk_create(repositoriesObjects)

    def getAllRepositories(self, repositories_url_request):
        repositories_request = requests.get(url=repositories_url_request, auth=self.auth)
        repositories_links = repositories_request.links

        if ('next' in repositories_links.keys()):
            self.getAllRepositories(repositories_links['next']['url'])

        self.repositories += repositories_request.json()

    def saveMembers(self, organization):
        members_request_url = 'https://api.github.com/orgs/' + organization.login + '/members'
        members_request = requests.get(url=members_request_url, auth=self.auth)

        membersObjects = []
        for members in members_request.json():
            membersObjects.append(Members(
                login=members['login'],
                avatar_url=members['avatar_url'] + '&s=96',
                html_url=members['html_url'],
                organization=organization,
            ))
        Members.objects.bulk_create(membersObjects)
