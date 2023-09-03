from django.db import models

# Definindo o modelo FilmeFavorito
class FilmeFavorito(models.Model):
    # Campos para armazenar valores
    titulo = models.CharField(max_length=100)
    diretor = models.CharField(max_length=100, blank=True, null=True)
    ano = models.PositiveIntegerField(blank=True, null=True)
    
    def __str__(self):
        # Método que retorna uma representação em string do objeto FilmeFavorito (o título do filme)
        return self.titulo

# Definindo o modelo Crud
class Crud(models.Model):
    # Campos para armazenar os dados do Usuario+
    id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=50, default="Nome Padrão")
    email = models.EmailField(max_length=50)
    numero = models.BigIntegerField()
    
    # Campo de relacionamento: armazena a relação com um objeto FilmeFavorito
    # on_delete=models.SET_NULL: Define o comportamento quando o FilmeFavorito relacionado é excluído (define para NULL)
    # blank=True, null=True: Permite que o campo seja opcional (pode ser deixado em branco ou nulo)
    filme_favorito = models.ForeignKey(FilmeFavorito, on_delete=models.SET_NULL, blank=True, null=True)
    
    def __str__(self):
        # Método que retorna uma representação em string do objeto Crud (o nome completo)
        return self.fullname
