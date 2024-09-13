# Projeto API Pessoa - Athenas

Este projeto implementa uma API RESTful para gerenciar a entidade `Pessoa`, com operações de **inclusão**, **alteração**, **exclusão** e **pesquisa** de dados, seguindo o padrão Controller → Service → Task. O projeto utiliza **Django** com **PostgreSQL** como banco de dados e está configurado para rodar em contêineres **Docker**.

## Pré-requisitos

- [Docker](https://www.docker.com/get-started) instalado no sistema
- [Docker Compose](https://docs.docker.com/compose/install/) instalado no sistema

## Configuração e Execução

```
docker-compose up --build
docker-compose exec web python manage.py migrate
```