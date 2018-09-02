from django.shortcuts import render, redirect
from django.views import View
from apps.organization.models import Organizations
from apps.member.models import Members


class Member(View):
    def get(self, request, organization_login=False):
        try:
            organization = Organizations.objects.get(login=organization_login)
            members = Members.objects.all()

        except Organizations.DoesNotExist:
            return redirect('repositories:index')

        return render(request, 'members/listing.html', {
            'section': 'members',
            'organization': organization,
            'repositories_cant': organization.repositories_set.count(),
            'members_cant': members.count(),

            'members': members
        })
