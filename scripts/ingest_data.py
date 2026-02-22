import yfinance as yf
import argparse
import os
import sys


def download_data(ticker, start, end):
    print(f"--- Iniciando Ingestão de Dados ---")
    print(f"Ticker: {ticker}")
    print(f"Período: {start} até {end}")

    try:
        # Download dos dados
        df = yf.download(ticker, start=start, end=end)

        if df.empty:
            print(
                f"Erro: Nenhum dado encontrado para {ticker}. \
                Verifique o símbolo ou as datas."
            )
            return

        # Garante que a pasta data existe
        # (subindo um nível se rodar de dentro de /scripts)
        output_dir = "data"
        os.makedirs(output_dir, exist_ok=True)

        filename = f"{output_dir}/{ticker}_history.csv"
        df.to_csv(filename)

        print(f"--- Sucesso! ---")
        print(f"Arquivo salvo em: {filename}")
        print(f"Total de linhas: {len(df)}")

    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Ingestão de dados históricos do Yahoo Finance"
    )

    # Argumentos posicionais
    parser.add_argument(
        "ticker", type=str, help="Símbolo da ação (ex: AAPL ou PETR4.SA)"
    )
    parser.add_argument("start", type=str, help="Data de início (AAAA-MM-DD)")
    parser.add_argument("end", type=str, help="Data de fim (AAAA-MM-DD)")

    args = parser.parse_args()

    download_data(args.ticker, args.start, args.end)
