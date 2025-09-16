from django.urls import path
from . import views

urlpatterns = [
    path('',views.listar_pokemons,name='listar_pokemons')
]