FROM python:3.13.0

# Desativando a criação de ambientes virtuais no Poetry
ENV POETRY_VIRTUALENVS_CREATE=false

# Definindo o diretório de trabalho
WORKDIR /app

# Copiando os arquivos do projeto
COPY . .

# Instalando o Poetry
RUN pip install poetry

# Configurando o Poetry
RUN poetry config installer.max-workers 10

# Instalando as dependências do projeto
RUN poetry install --no-interaction --no-ansi

# Expondo a porta 8000
EXPOSE 8000

# Comando para iniciar o FastAPI usando Uvicorn
CMD ["poetry", "run", "uvicorn", "fm_fastapi.app:app", "--host", "0.0.0.0", "--port", "8000"]
