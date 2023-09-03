from rest_framework import serializers
from .models import Crud, FilmeFavorito

# Define um serializador para o modelo Crud
class CrudSerializer(serializers.ModelSerializer):
    class Meta:
        # Especifica o modelo que este serializador está associado
        model = Crud 
        # Lista os campos que devem ser incluídos na serialização
        # Aqui, '__all__' significa que todos os campos do modelo serão incluídos
        fields = '__all__'

# Define um serializador para o modelo FilmeFavorito 
class FilmeFavoritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilmeFavorito  
        fields = '__all__'