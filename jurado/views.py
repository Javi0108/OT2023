from django.shortcuts import get_object_or_404, render

from .models import Jurado


def jurado_list(request):
    jurados = Jurado.objects.all()
    return render(request, 'jurados/list.html', {'jurados': jurados})


def jurado_detail(request, jurado_slug: str):
    jurado = get_object_or_404(Jurado, slug=jurado_slug)
    return render(request, 'jurados/detail.html', {'jurado': jurado})
