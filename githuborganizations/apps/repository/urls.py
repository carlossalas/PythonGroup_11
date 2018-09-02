from django.urls import path
from apps.repository import views

app_name = 'repository'
urlpatterns = [
    path('', views.Repository.as_view(), name='index')
]
