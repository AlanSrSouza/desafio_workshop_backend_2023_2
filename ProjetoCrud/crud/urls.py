from django.urls import path
from .views import Nome_do_Usuario, Atualizar_ou_Excluir_Usuario, Nome_do_Filme, Atualizar_ou_Excluir_Filme #Importando classes para refenrencialas a links

urlpatterns = [
    path('crud/', Nome_do_Usuario.as_view(), name="crud-Create-User-List"),  # Nome exclusivo para CRUD
    path('crud/<int:pk>', Atualizar_ou_Excluir_Usuario.as_view(), name='crud-user-Details'),  # Nome exclusivo para CRUD
    path('filme/', Nome_do_Filme.as_view(), name="filme-Create-User-List"),  # Nome exclusivo para Filmes Favoritos
    path('filme/<int:pk>', Atualizar_ou_Excluir_Filme.as_view(), name='filme-user-Details'),  # Nome exclusivo para Filmes Favoritos
]