from django.shortcuts import get_object_or_404, render

from .models import Alumnado


def alumnado_list(request):
    alumnados = Alumnado.objects.all()
    return render(request, 'alumnados/list.html', {'alumnados': alumnados})


def alumnado_detail(request, alumnado_slug: str):
    alumnado = get_object_or_404(Alumnado, slug=alumnado_slug)
    music_style = alumnado.music_style.all()
    return render(
        request, 'alumnados/detail.html', {'alumnado': alumnado, 'music_style': music_style}
    )
