# Versão estável e recomendada para workloads de ML
FROM python:3.11-slim

# Define o diretório de trabalho
WORKDIR /app

# Instala dependências mínimas do sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copia e instala as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia os artefatos (.keras e .pkl) e o código
COPY . .

# Porta padrão do FastAPI
EXPOSE 8000

# Comando para rodar a aplicação
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]