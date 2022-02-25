from django.urls import path
from . import views

app_name = 'dust_checker'

urlpatterns = [
    path('', views.index, name='index'),
    path('/detail', views.detail, name='detail'),
]