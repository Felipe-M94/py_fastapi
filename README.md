# Py FastAPI

**Py FastAPI** é uma aplicação backend construída com **FastAPI**, oferecendo uma solução robusta para a criação de APIs RESTful. O projeto utiliza **PostgreSQL** como banco de dados, gerenciado via Docker, e integra **SQLAlchemy** como ORM, com suporte a migrações usando **Alembic**. A autenticação é implementada com **JWT**, e a validação de dados é feita com **Pydantic**.

## Funcionalidades Principais

- **FastAPI** para desenvolvimento rápido de APIs.
- **SQLAlchemy** como ORM para gerenciar interações com o banco de dados.
- **Alembic** para migrações do banco de dados.
- **JWT** para autenticação segura.
- **Docker Compose** para orquestrar containers, incluindo o **PostgreSQL**.
- **Pydantic** para validação de dados e configurações.
- **Ruff** para linting e **pytest** para testes automatizados.

## Tecnologias Utilizadas

- **Python 3.13**: Linguagem principal.
- **FastAPI**: Framework para criação de APIs.
- **SQLAlchemy**: ORM para PostgreSQL.
- **Alembic**: Sistema de migração para bancos de dados.
- **PostgreSQL**: Banco de dados relacional.
- **JWT**: Autenticação via JSON Web Tokens.
- **Pydantic Settings**: Gerenciamento e validação de configurações.
- **Docker Compose**: Orquestração de containers (incluindo PostgreSQL).
- **Ruff**: Linting de código.
- **pytest**: Framework para testes.

## Como Rodar Manualmente

1. Clone o repositório:
   ```bash
   git clone https://github.com/Felipe-M94/py_fastapi.git

2. Instale as dependências:
   ```bash
   poetry install

3. Execute o servidor:
   ```bash
   task run

4. Execute os testes:
   ```bash
   task test

## Como Rodar via Docker

1. Clone o repositório:
   ```bash
   git clone https://github.com/Felipe-M94/py_fastapi.git

2. Inicie o ambiente Docker para rodar o PostgreSQL e o APP:
   ```bash
   docker-compose up --build


