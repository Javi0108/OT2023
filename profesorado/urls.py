from django.urls import path

from . import views

app_name = 'profesorado'

urlpatterns = [
    path('', views.profesorado_list, name='profesorado_list'),
    path('<slug:profe_slug>/', views.profesorado_detail, name='profesorado_detail'),
]
