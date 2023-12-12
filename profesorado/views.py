from django.shortcuts import get_object_or_404, render

from .models import Profesorado


def dashboard(request):
    return render(request, 'dashboard.html', {'section': 'dashboard'})


def live(request):
    return render(request, 'live.html', {'section': 'live'})


def profesorado_list(request, profe_str: str = None):
    if profe_str is None:
        profes = Profesorado.objects.all()
    else:
        profes = Profesorado.objects.filter(profe_str)

    return render(request, 'profes/list.html', {'profes': profes})


def profesorado_detail(request, profe_slug: str):
    profe = get_object_or_404(Profesorado, slug=profe_slug)
    return render(request, 'profes/detail.html', {'profe': profe})
