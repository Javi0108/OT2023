from django.urls import path

from . import views

app_name = 'profesorado'
urlpatterns = [
    # post views
    path('', views.profesorado_list, name='profesorado_list'),
    # path('<str:name>/', views.profesorado_detail, name='profesorado_detail'),
]
