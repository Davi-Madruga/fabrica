from django.urls import path
from . import views

urlpatterns = [
    path('',views.listar_pokemons,name='listar_pokemons'),
    path('criar_pokemon/',views.criar_pokemon,name='criar_pokemon'),
    path('atualizar_pokemon/<int:pk>/',views.atualizar_pokemon,name='atualizar_pokemon'),
    path('deletar_pokemon/<int:pk>/',views.deletar_pokemon,name='deletar_pokemon'),
    path('detalhar_pokemon/<int:pk>/',views.detalhar_pokemon,name='detalhar_pokemon'),
]