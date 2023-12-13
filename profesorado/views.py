from django.shortcuts import get_object_or_404, render
from django.apps import apps

from .models import Profesorado


def dashboard(request):
    return render(request, 'dashboard.html', {'section': 'dashboard'})


def live(request):
    return render(request, 'live.html', {'section': 'live'})


def profesorado_list(request):
    profes = Profesorado.objects.all()
    return render(request, 'profes/list.html', {'profes': profes})


def profesorado_detail(request, profe_slug: str):
    profe = get_object_or_404(Profesorado, slug=profe_slug)
    return render(request, 'profes/detail.html', {'profe': profe})


# def search(request, search_str:str = None):
#     resultados  = {}
    
#     # Obtener todos los modelos registrados en la aplicación Django
#     modelos = apps.get_models()

#     # Iterar sobre los modelos y realizar una consulta para cada uno
#     for modelo in modelos:
#         # Obtener el nombre de la tabla asociada al modelo
#         nombre_tabla = modelo._meta.db_table

#         # Realizar la consulta utilizando el método filter
#         datos_tabla = modelo.objects.filter(search_str__icontains=search_str)

#         # Almacenar los res en un diccionario
#         resultados[nombre_tabla] = list(datos_tabla.values())
#     return render(request, 'search.html', {'search': resultados})
