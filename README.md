# Pizzaria Django Website

![Imagem do Site][site]

Este site foi desenvolvido como projeto para a disciplina de Programação WEB da Universidade Federal de Lavras. O site tem a temática de uma pizzaria do DCC e foi desenvolvido utilizando o framework Django. O site permite que os usuários visualizem o menu de pizzas disponíveis, façam pedidos e acompanhem o status dos pedidos.

## Requisitos

- Python 3.x
- Django 4.2.1

## Instalação

1. Clone o repositório para o seu ambiente local:

```shell
git clone https://github.com/rafaelportomoura/pizzaria-backend-py.git
```

2. Acesse o diretório do projeto:

```shell
cd pizzaria-backend-py
```

3. Crie um ambiente virtual (opcional):

```shell
python3 -m venv env
source env/bin/activate
```

4. Instale as dependências do projeto:

```shell
pip install -r requirements.txt
```

## Criando super usuário

1. Execute o comando para criar super usuário:

```shell
python manage.py createsuperuser
```

## Rodando o Projeto

1. Execute as migrações do banco de dados:

```shell
python manage.py migrate
```

2. Inicie o servidor de desenvolvimento:

```shell
python manage.py runserver
```

3. Acesse o site no seu navegador em [http://localhost:8000](http://localhost:8000).

## Referências

1. [Django][djangoproject]
2. [Jinja][jinja]
3. [Ambiente Virtual no Python (Alura)][alura]

<!-- LINKS -->

[alura]: https://www.alura.com.br/artigos/ambientes-virtuais-em-python?gclid=EAIaIQobChMI8qTH16jp_gIVfWpvBB21_QsdEAAYASAAEgIwI_D_BwE
[djangoproject]: https://docs.djangoproject.com/en/4.2/
[jinja]: https://jinja.palletsprojects.com/en/3.1.x/
[site]: ./assets/site.png
