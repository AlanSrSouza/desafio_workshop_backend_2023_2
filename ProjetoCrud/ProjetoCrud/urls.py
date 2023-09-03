from django.contrib import admin
from django.urls import path, include

# Configuração das URLs da aplicação Django
urlpatterns = [
    # Define uma URL para a página de administração do Django
    path('admin/', admin.site.urls),
    # Define uma URL para incluir as URLs da sua aplicação 'crud'
    path('api/', include('crud.urls')),
]