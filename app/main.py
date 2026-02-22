import os
import numpy as np
import tensorflow as tf
import joblib
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

# 1. Inicialização do App
app = FastAPI(title="Stock Prediction API - Noah Diunkz")


# 2. Definição do Modelo de Entrada
class StockInput(BaseModel):
    prices: List[float]  # Lista com os últimos 60 preços


# 3. Carregamento dos Artefatos
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "saved_models", "lstm_model.keras")
SCALER_PATH = os.path.join(BASE_DIR, "saved_models", "scaler.pkl")

try:
    model = tf.keras.models.load_model(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    print("Sucesso: Modelo e Scaler carregados.")
except Exception as e:
    print(f"Erro ao carregar arquivos: {e}")
    model = None
    scaler = None


@app.get("/")
def home():
    return {"status": "Online", "modelo_carregado": model is not None}


@app.post("/predict")
def predict(data: StockInput):
    if len(data.prices) != 60:
        raise HTTPException(status_code=400, detail="Envie exatamente 60 preços.")

    try:
        # Prepara os dados (Reshape -> Scale -> Reshape para LSTM)
        input_data = np.array(data.prices).reshape(-1, 1)
        input_scaled = scaler.transform(input_data)
        input_final = input_scaled.reshape(1, 60, 1)

        # Predição e inversão da escala
        pred_scaled = model.predict(input_final)
        pred_final = scaler.inverse_transform(pred_scaled)

        return {"prediction": float(pred_final[0][0]), "ticker": "AAPL"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
