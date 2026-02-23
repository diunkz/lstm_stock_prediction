# LSTM - Stock Prediction 📈

O objetivo deste projeto é desenvolver um modelo preditivo utilizando redes neurais LSTM (Long Short Term Memory) para prever o valor de fechamento de ações.

O projeto abrange desde a ingestão de dados, pré-processamento de séries temporais, treinamento de modelo e disponibilização via API containerizada com monitoramento em tempo real.

## 🏗️ Arquitetura da Solução

O fluxo de dados foi projetado para ser modular e reprodutível, utilizando o padrão de microserviços:

1. Ingestão (scripts/): Script Python que consome dados históricos via yfinance e armazena em CSV.
2. Treinamento (notebooks/): Pipeline de Ciência de Dados incluindo limpeza, normalização com MinMaxScaler, estruturação de janelas temporais de 60 dias e treinamento da rede LSTM.
3. Artefatos (app/saved_models/): Exportação do modelo treinado (.keras) e do escalonador (.pkl).
4. Serviço (app/): API FastAPI que carrega os artefatos e expõe endpoints de predição e métricas.
5. Observabilidade: Stack composta por Prometheus para coleta de métricas e Grafana para visualização de performance.
6. Orquestração (Docker): Containerização completa para garantir a paridade de ambiente, otimizada para arquitetura Apple Silicon (M4).

---

## 📂 Estrutura do Projeto

* app/
  * main.py (Servidor FastAPI com lógica de inferência e instrumentação de métricas)
  * Dockerfile (Receita do container Python 3.13-slim)
  * requirements.txt (Dependências da API e Prometheus)
  * saved_models/ (Artefatos do modelo)
* data/ (Base de dados histórica em CSV)
* monitoring/
  * prometheus.yml (Configuração de coleta de dados do Prometheus)
* notebooks/
  * training.ipynb (Desenvolvimento do modelo e validação)
* scripts/
  * ingest_data.py (Coleta de dados)
  * generate_test_json.py (Utilitário para massa de dados de teste)
* docker-compose.yml (Orquestrador multi-container: API, Prometheus e Grafana)

---

## 🚀 Como Rodar o Projeto

### Pré-requisitos
* Docker e Docker Compose instalados.

### 1. Subir a Stack Completa
Na raiz do projeto, execute o comando abaixo para construir as imagens e subir os serviços:

docker compose up --build

A stack estará disponível nos seguintes endereços:
* API FastAPI: http://localhost:8000
* Prometheus: http://localhost:9090
* Grafana: http://localhost:3000 (Login padrão: admin/admin)

### 2. Gerar Dados de Teste
Para testar a API com os dados reais mais recentes, utilize o script auxiliar:

python scripts/generate_test_json.py

---

## 🧪 Testando a Predição

### Interface Swagger (Visual)
Acesse http://localhost:8000/docs, utilize o endpoint POST /predict e cole o conteúdo do arquivo app/test_input.json.

### Via Terminal (cURL)
curl -X 'POST' 'http://localhost:8000/predict' -H 'Content-Type: application/json' -d @app/test_input.json

---

## 📊 Monitoramento e Escalabilidade

O projeto atende aos requisitos de monitoramento e escalabilidade através de:
* Rastreio de Performance: Coleta automática de latência de resposta e contagem de requisições por segundo via Prometheus.
* Visualização: Dashboard no Grafana para acompanhamento da saúde da aplicação em tempo real.
* Escalabilidade: Deploy containerizado facilitando o escalonamento horizontal e o uso de orquestradores como Kubernetes.
* Recursos: Monitoramento de utilização de CPU e Memória via comando 'docker stats'.

---

## ⚙️ Detalhes Técnicos do Modelo

* Algoritmo: LSTM (Long Short Term Memory) com camadas de Dropout (0.2).
* Input: Janelas deslizantes de 60 dias (Window Size).
* Performance: O modelo atingiu um MAE (Erro Médio Absoluto) de aproximadamente 3.13.

---