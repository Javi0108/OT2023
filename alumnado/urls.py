from django.urls import path

from . import views

app_name = 'alumnado'

urlpatterns = [
    path('', views.alumnado_list, name='alumnado_list'),
    path('<slug:alumnado_slug>/', views.alumnado_detail, name='alumnado_detail'),
]
