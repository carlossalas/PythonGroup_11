from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from githuborganizations.views import Main
from apps.organization.models import Organizations
from apps.repository.forms import FilterForm


class Repository(Main, View):
    def get(self, request, organization_login=False):
        try:
            organization = Organizations.objects.get(login=organization_login)

            q = request.GET.get('q', '')
            sort = request.GET.get('sort', 'newest')
            order_by = '-' if sort == 'newest' else ''

            repositories = organization.repositories_set.filter(name__contains=q)
            repositories = repositories.order_by(order_by + 'created_at')

            repositories_cant = repositories.count()
            members_cant = organization.members_set.count()
        except Organizations.DoesNotExist:
            return HttpResponseRedirect(reverse('organization:index'))

        return render(request, 'repositories/listing.html', {
            'section': 'repositories',
            'organization': organization,
            'repositories': repositories,
            'repositories_cant': repositories_cant,
            'members_cant': members_cant,
            'form': FilterForm({'q': q, 'sort': sort})
        })
