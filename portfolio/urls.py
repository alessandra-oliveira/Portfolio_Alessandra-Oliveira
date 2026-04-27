from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.home, name = 'home'),
    path('projetos/', views.projetos, name = 'projetos'), #dando um app_name: evita conflitos com urls com o mesmo nome de rota
    path('contato/', views.contato, name = 'contato')
]