from django.shortcuts import get_object_or_404, render

from .models import Alumnado, MusicStyle


def alumnado_list(request, alumnado_str: str = None):
    if alumnado_str is None:
        alumnados = Alumnado.objects.all()
    else:
        alumnados = Alumnado.objects.filter(alumnado_str)
    return render(request, 'alumnados/list.html', {'alumnados': alumnados})


def alumnado_detail(request, alumnado_slug: str):
    alumnado = get_object_or_404(Alumnado, slug=alumnado_slug)
    music_style = MusicStyle.objects.all()
    return render(
        request, 'alumnados/detail.html', {'alumnado': alumnado, 'music_style': music_style}
    )
