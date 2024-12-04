FROM python:3.13.0

# Desativando a criação de ambientes virtuais no Poetry
ENV POETRY_VIRTUALENVS_CREATE=false

# Definindo o diretório de trabalho
WORKDIR /app

# Copiando os arquivos do projeto para o contêiner
COPY . .

# Instalando o Poetry
RUN pip install poetry

# Configurando o Poetry
RUN poetry config installer.max-workers 10

# Instalando as dependências do projeto
RUN poetry install --no-interaction --no-ansi

# Tornando o entrypoint.sh executável
RUN chmod +x /app/entrypoint.sh

# Expondo a porta 8000
EXPOSE 8000

# Definindo o entrypoint para o script de inicialização
ENTRYPOINT ["/app/entrypoint.sh"]
