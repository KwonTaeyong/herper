from django.shortcuts import render
from .api import check_ground


# Create your views here.

def index(request):
    res = check_ground()
    pm10 = res.get('공원')
    context = {'station': '공원', 'pm10': pm10}
    return render(request, 'ground_checker/ground_main.html', context)


def detail(request):
    res = check_ground()
    context = {'ground': res}
    return render(request, 'ground_checker/ground_detail.html', context)

