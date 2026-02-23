import pandas as pd
import json
import os


def generate_json():
    # Caminho para o seu CSV de histórico
    csv_path = os.path.join(os.path.dirname(__file__), "../data/AAPL_history.csv")
    output_path = os.path.join(os.path.dirname(__file__), "../app/test_input.json")

    try:
        # Lê o CSV tratando o MultiIndex do yfinance
        df = pd.read_csv(csv_path, header=[0, 1], index_col=0)

        # Extrai os últimos 60 preços de fechamento (Close) da Apple (AAPL)
        # Usamos .tail(60) para pegar os dados mais recentes do arquivo
        last_60_prices = df["Close"]["AAPL"].tail(60).tolist()

        # Monta o dicionário no formato que a API (FastAPI) espera
        payload = {"prices": last_60_prices}

        # Salva em um arquivo JSON na pasta app para facilitar o acesso
        with open(output_path, "w") as f:
            json.dump(payload, f, indent=4)

        print(f"✅ JSON de teste gerado com sucesso em: {output_path}")
        print(f"📊 Foram coletados os últimos {len(last_60_prices)} preços do CSV.")

    except Exception as e:
        print(f"❌ Erro ao gerar o JSON: {e}")


if __name__ == "__main__":
    generate_json()
