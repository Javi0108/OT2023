from django.shortcuts import get_object_or_404, render

from .models import Profesorado


def dashboard(request):
    return render(request, 'dashboard.html', {'section': 'dashboard'})


def profesorado_list(request):
    profes = Profesorado.objects.all()
    return render(request, 'profes/list.html', {'profes': profes})


def profesorado_detail(request, profe_slug: str):
    profe = get_object_or_404(Profesorado, slug=profe_slug)
    return render(request, 'profes/detail.html', {'profe': profe})
