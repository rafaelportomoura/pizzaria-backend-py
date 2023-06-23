# Pizzaria Django Website

![Imagem do Site][site]

Este site foi desenvolvido como projeto para a disciplina de Programação WEB da Universidade Federal de Lavras. O site tem a temática de uma pizzaria do DCC e foi desenvolvido utilizando o framework Django. O site permite que os usuários visualizem o menu de pizzas disponíveis, façam pedidos e acompanhem o status dos pedidos.

## Requisitos

- Docker version 24.0.0
- Docker Compose version 2.18.1

## Instalação

1. Clone o repositório para o seu ambiente local:

```shell
git clone https://github.com/rafaelportomoura/ufla-pizzaria-django.git
```

2. Acesse o diretório do projeto:

```shell
cd ufla-pizzaria-django
```

3. Crie um arquivo `.env` no diretório raiz do projeto com as seguintes variáveis de ambiente, substituindo o que tiver entre `{}`

```.env
POSTGRES_DB={nome_do_banco}
POSTGRES_USER={usuario}
POSTGRES_PASSWORD={senha}
DB_HOST_NAME=db
LC_COLLATE=pt_BR.UTF-8
LC_CTYPE=pt_BR.UTF-8
```

4. Crie um arquivo `.env` no diretório raiz do projeto com as seguintes variáveis de ambiente, substituindo o que tiver entre `{}`

```.env
RABBITMQ_DEFAULT_USER={user}
RABBITMQ_DEFAULT_PASS={pass}
RABBITMQ_HOST=rabbitmq
```

## Rodando o Projeto

1. Inicie o contêiner do PostgreSQL e o servidor Django executando o seguinte comando:

```shell
docker-compose up
```

Isso irá construir a imagem do Docker e iniciar o contêiner do PostgreSQL juntamente com o servidor Django e o Administrador do banco de dados.

2. Acesse o site no seu navegador em [http://localhost:8000](http://localhost:8000).
3. Acesse o ambiente de administrador no seu navegador em [http://localhost:8000/admin](http://localhost:8000/admin).

## Criando super usuário

1. Execute o comando para criar super usuário:

```shell
docker-compose exec pizzaria python manage.py createsuperuser
```

## Referências

1. [Django][djangoproject]
2. [Jinja][jinja]
3. [Ambiente Virtual no Python (Alura)][alura]
4. [Django Command][django-command]
<!-- LINKS -->

[alura]: https://www.alura.com.br/artigos/ambientes-virtuais-em-python?gclid=EAIaIQobChMI8qTH16jp_gIVfWpvBB21_QsdEAAYASAAEgIwI_D_BwE
[djangoproject]: https://docs.djangoproject.com/en/4.2/
[jinja]: https://jinja.palletsprojects.com/en/3.1.x/
[site]: ./assets/site.png
[django-command]: https://docs.djangoproject.com/en/4.2/howto/custom-management-commands/
