from django.shortcuts import render

from .models import Profesorado


def dashboard(request):
    return render(request, 'dashboard.html', {'section': 'dashboard'})


def profesorado_list(request):
    profes = Profesorado.objects.all()
    return render(request, 'profes/list.html', {'profes': profes})


# def profesorado_detail():
