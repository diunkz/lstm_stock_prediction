# Utiliza a imagem oficial do Python 3.11 Slim por ser mais estável para ML em containers
FROM python:3.11-slim

# Define a pasta principal onde os comandos serão executados dentro do container
WORKDIR /app

# Instala pacotes essenciais do Linux para compilação de bibliotecas (necessário para ML)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Primeiro, copia apenas o arquivo de dependências (otimiza o cache de camadas do Docker)
COPY app/requirements.txt .

# Instala todas as bibliotecas (FastAPI, TensorFlow-CPU, etc.)
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código da pasta app (main.py e pasta saved_models) para dentro do WORKDIR
COPY app/ .

# Informa ao Docker que o container receberá conexões na porta 8000
EXPOSE 8000

# Comando de inicialização usando o Uvicorn como servidor ASGI
# --host 0.0.0.0 é obrigatório para que a API aceite conexões externas ao container
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]