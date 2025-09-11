from django.urls import path
from .views import listar_pessoa,criar_pessoa,deletar_pessoa,atualizar_pessoa

urlpatterns = [
    path('',listar_pessoa,name='listar'),
    path('criar/',criar_pessoa,name='criar'),
    path('deletar/<int:pk>',deletar_pessoa,name='deletar_pessoa'),
    path('atualizar/<int:pk>',atualizar_pessoa,name='atualizar_pessoa'),
]
