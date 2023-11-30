from django.urls import path

from . import views

app_name = 'jurado'

urlpatterns = [
    path('', views.jurado_list, name='jurado_list'),
    path('<slug:jurado_slug>/', views.jurado_detail, name='jurado_detail'),
]
