# Fullstack Challenge Django

Este é um projeto fullstack criado como parte de um desafio de desenvolvimento. A aplicação envolve um frontend desenvolvido em Angular que se comunica com um backend Django para realizar operações CRUD (Criar, Ler, Atualizar, Excluir) sobre uma entidade chamada `Pessoa`. O projeto também inclui uma funcionalidade extra para calcular o peso ideal de uma pessoa com base na altura.

## Estrutura do Projeto

- **Backend:** Django, seguindo o padrão Controller → Service → Task com PostgreSQL. Está configurado para rodar em contêineres Docker.

## Funcionalidades

O projeto implementa uma API RESTful para gerenciar a entidade `Pessoa`, com operações de:
1. **Incluir**: Adicionar novas pessoas ao sistema.
2. **Alterar**: Atualizar as informações de uma pessoa existente.
3. **Excluir**: Remover pessoas cadastradas.
4. **Pesquisar**: Buscar por pessoas já cadastradas.
5. **Calcular Peso Ideal**: Baseado na fórmula do peso ideal para homens e mulheres.
   
## Pré-requisitos

- [Docker](https://www.docker.com/get-started) instalado no sistema
- [Docker Compose](https://docs.docker.com/compose/install/) instalado no sistema

## Instalação

Siga as etapas abaixo para configurar e rodar a aplicação localmente:

1. Clone o repositório:
    ```bash
    git clone <git@github.com:GeovanaAugusta/fullstack-challenge-django.git>
    cd fullstack-challenge-django
    ```

2.  Construa e inicialize os contêineres Docker:
    ```bash
    docker-compose up --build
    ```

3. Aplique as migrações do banco de dados:
    ```bash
    docker-compose exec web python manage.py migrate
    ```

   O backend estará acessível em `http://localhost:8000`.

