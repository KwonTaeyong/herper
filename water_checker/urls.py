from django.urls import path
from . import views

app_name = 'water_checker'

urlpatterns = [
    path('', views.index, name='index'),
    path('/detail', views.detail, name='detail'),
]