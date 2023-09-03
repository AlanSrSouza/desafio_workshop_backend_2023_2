from django.shortcuts import render
from rest_framework import generics
from .models import Crud, FilmeFavorito
from .serializers import CrudSerializer, FilmeFavoritoSerializer

# Defina uma view para listar e criar objetos Crud
class Nome_do_Usuario(generics.ListCreateAPIView):
    # Consulta para obter todos os objetos Crud
    queryset = Crud.objects.all()
    # Serializer usado para serializar e desserializar objetos Crud
    serializer_class = CrudSerializer

# Defina uma view para recuperar, atualizar e excluir objetos Crud por ID
class Atualizar_ou_Excluir_Usuario(generics.RetrieveUpdateDestroyAPIView):
    # Consulta para obter todos os objetos Crud
    queryset = Crud.objects.all()
    serializer_class = CrudSerializer

# Defina uma view para listar e criar objetos FilmeFavorito
class Nome_do_Filme(generics.ListCreateAPIView):
    # Consulta para obter todos os objetos FilmeFavorito
    serializer_class = FilmeFavoritoSerializer

# Defina uma view para recuperar, atualizar e excluir objetos FilmeFavorito por ID
class Atualizar_ou_Excluir_Filme(generics.RetrieveUpdateDestroyAPIView):
    # Consulta para obter todos os objetos FilmeFavorito
    queryset = FilmeFavorito.objects.all()
    serializer_class = FilmeFavoritoSerializer