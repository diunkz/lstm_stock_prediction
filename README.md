# LSTM - Stock Prediction 📈

O objetivo deste projeto é desenvolver um modelo preditivo utilizando redes neurais LSTM (Long Short Term Memory) para prever o valor de fechamento das ações.

O projeto abrange desde a ingestão de dados, pré-processamento de séries temporais, treinamento de modelo e disponibilização via API containerizada.

## 🏗️ Arquitetura da Solução

O fluxo de dados foi projetado para ser modular e reprodutível, seguindo as melhores práticas de Engenharia de Dados:

1. Ingestão (scripts/): Script Python que consome dados históricos via yfinance e armazena em CSV.
2. Treinamento (notebooks/): Pipeline de Ciência de Dados incluindo limpeza, normalização com MinMaxScaler, estruturação de janelas temporais de 60 dias e treinamento da rede LSTM.
3. Artefatos (app/saved_models/): Exportação do modelo treinado no formato nativo .keras e do escalonador em .pkl.
4. Serviço (app/): API FastAPI que carrega os artefatos e expõe um endpoint de predição.
5. Orquestração (Docker): Containerização completa da API para garantir a paridade de ambiente entre desenvolvimento e produção.

---

## 📂 Estrutura do Projeto

* **app/**
  * main.py (Servidor FastAPI com lógica de inferência)
  * Dockerfile (Receita do container Python 3.11-slim)
  * requirements.txt (Dependências da API)
  * saved_models/ (Artefatos: lstm_model.keras e scaler.pkl)
* **data/** (Base de dados histórica em CSV)
* **notebooks/**
  * training.ipynb (Notebook de treinamento, validação e gráficos)
* **docker-compose.yml** (Orquestrador de serviços)
* **scripts/**
  * ingest_data.py (Script de coleta de dados via yfinance)
  * generate_test_json.py (Script para extrair massa de teste do CSV)

---
## 🚀 Como Rodar o Projeto

### Pré-requisitos
* Docker e Docker Compose instalados.
* Python 3.11+ (caso deseje rodar scripts fora do container).

### 1. Construir e Subir a API
Na raiz do projeto, execute o comando abaixo:

docker compose up --build

A API estará disponível em: http://localhost:8000

### 2. Gerar Dados de Teste
Para testar a API com os dados reais mais recentes contidos no seu CSV, utilize o script auxiliar:

python scripts/generate_test_json.py

Isso criará automaticamente o arquivo app/test_input.json contendo os últimos 60 preços de fechamento.

---

## 🧪 Testando a Predição

Você pode validar o funcionamento da API de duas formas:

### Interface Swagger (Visual)
1. Acesse http://localhost:8000/docs.
2. Clique no endpoint POST /predict.
3. Selecione Try it out.
4. Cole o conteúdo do arquivo app/test_input.json no corpo da requisição e execute.

### Via Terminal (cURL)
curl -X 'POST' 'http://localhost:8000/predict' -H 'Content-Type: application/json' -d @app/test_input.json

---

## 📊 Detalhes Técnicos do Modelo

* Algoritmo: LSTM (Long Short Term Memory) com camadas de Dropout (0.2).
* Input: Janelas deslizantes de 60 dias (Window Size).
* Performance: O modelo atingiu um MAE (Erro Médio Absoluto) de aproximadamente 3.13.
* Banda de Erro: As visualizações geradas no notebook incluem uma margem de confiança baseada no MAE para análise de volatilidade.

---
Autor: Noah Diunkz