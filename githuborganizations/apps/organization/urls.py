from django.urls import path
from apps.organization import views

app_name = 'organization'
urlpatterns = [
    path('', views.Organization.as_view(), name='index'),
    path('importar/<slug:organization_login>', views.Import.as_view(), name='import')
]
