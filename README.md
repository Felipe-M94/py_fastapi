# Py FastAPI

Este projeto é uma aplicação backend desenvolvida utilizando **FastAPI**, uma framework Python moderna e rápida para a criação de APIs. Ele utiliza integração com **SQLAlchemy** para gerenciamento de banco de dados, além de ferramentas de segurança e validação com **Pydantic**.

## Tecnologias Utilizadas

- **Python 3.13**: Linguagem de programação base.
- **FastAPI**: Framework para criação de APIs RESTful.
- **SQLAlchemy**: ORM para interação com banco de dados.
- **Alembic**: Migração de banco de dados.
- **PyJWT**: Autenticação JWT.
- **Pydantic-Settings**: Gerenciamento de configurações.
- **Ruff** e **Pytest**: Ferramentas para linting e testes.

## Estrutura de Tarefas

O projeto utiliza **Taskipy** para gerenciar tarefas comuns, incluindo:
- **Rodar o servidor**: `task run`
- **Executar testes**: `task test`
- **Linting**: `task lint`
- **Formatação de código**: `task format`

## Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/Felipe-M94/py_fastapi.git

2. Instale as dependências:
   ```bash
   poetry install

3. Execute o servidor:
   ```bash
   task run
