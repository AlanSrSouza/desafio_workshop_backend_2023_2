# Desafio Final Fábrica de Software
## Meu filme favorito
O Meu filme favorito é um site que oferece uma ampla possibilidade para os usuários selecionarem seus filmes favoritos. Escolha, encontre e salve seus filmes faritos.

## Tópicos

- [Inicialização](#inicialização)
- [Uso](#uso)
- [Contato](#contato)

## Inicialização
O comando abaixo usado no Django para criar arquivos de migração.
```
python manage.py makemigrations
```
O comando abaixo serve para aplicar as migrações pendentes ao banco de dados.
```
python manage.py migrate
```
O comando abaixo usado para iniciar o servidor de desenvolvimento embutido do Django. Quando você executa esse comando, o Django inicia um servidor web local que permite que você teste e desenvolva sua aplicação Django de forma fácil e conveniente.
```
python manage.py runserver
```

# Uso


 - Autenticação
A API requer autenticação para acessar recursos protegidos. Você pode autenticar-se usando o Token de Autenticação ou o superusuário.

- Token de Autenticação: Faça uma solicitação POST para http://localhost:8000/api/crud/.


### Endpoints da API
A API possui os seguintes endpoints:

- ### Usuários:

- Lista de Usuários: localhost/api/crud/
- Detalhes do Usuário: localhost/api/crud/{id}/
- Criar Usuário: localhost/api/users/
- Atualizar Usuário: localhost/api/crud/{id}/
- Deletar Usuário: localhost/api/crud/{id}/
---
- ### Filmes:

- Lista de Filmes: localhost/api/filmes/
- Detalhes do Filmes: localhost/api/filmes/{id}/
-Criar Filmes: localhost/api/filmes/
- Atualizar Filmes: localhost/filmes/{id}/
- Deletar Filmes: localhost/api/filmes/{id}/

Certifique-se de incluir o cabeçalho de autenticação ao acessar os endpoints protegidos.


## Contato
 
  - ### Gmail: alansoares20014@gmail.com
  - ### Linkedin: https://www.linkedin.com/in/alan-soares-de-souza-97a3a8242