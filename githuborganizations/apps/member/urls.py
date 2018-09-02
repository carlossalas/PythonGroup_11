from django.urls import path
from apps.member import views

app_name = 'member'
urlpatterns = [
    path('', views.Member.as_view(), name='index')
]
