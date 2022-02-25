from django.urls import path
from . import views

app_name = 'covid_checker'

urlpatterns = [
    path('', views.index, name='index')
]