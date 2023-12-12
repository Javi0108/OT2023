from django.shortcuts import get_object_or_404, render

from .models import Jurado


def jurado_list(request, jurado_str: str = None):
    if jurado_str is None:
        jurados = Jurado.objects.all()
    else:
        jurados = Jurado.objects.filter(jurado_str)
    return render(request, 'jurados/list.html', {'jurados': jurados})


def jurado_detail(request, jurado_slug: str):
    jurado = get_object_or_404(Jurado, slug=jurado_slug)
    return render(request, 'jurados/detail.html', {'jurado': jurado})
