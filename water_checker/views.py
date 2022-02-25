from django.shortcuts import render
from .api import check_water


# Create your views here.

def index(request):
    return render(request, 'water_checker/water_main.html')


def detail(request):
    res = check_water()
    context = {'water': res}
    return render(request, 'water_checker/water_detail.html', context)
