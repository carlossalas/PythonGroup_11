from django.contrib import admin
from apps.devs.models import Company, Software, Developer

admin.site.register(Company)
admin.site.register(Software)
admin.site.register(Developer)
