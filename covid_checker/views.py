from django.shortcuts import render



def index(request):

    return render(request, 'covid_checker/covid_main.html')

