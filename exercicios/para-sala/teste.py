import pandas as pd

# Importar os arquivos CSV usando pandas
try:
    df1 = pd.read_csv("abril-2024.csv")
    df2 = pd.read_csv("maio-2024.csv")
    
    # Concatenar os DataFrames
    resultado = pd.concat([df1, df2])

    # Salvar o resultado em um novo arquivo CSV
    resultado.to_csv("abril-maio-2024_pandas.csv", index=False)

    # Mensagem de confirmação
    print("Arquivo 'abril-maio-2024_pandas.csv' criado com sucesso.")
    
except FileNotFoundError as e:
    print(f"Erro: {e}. Verifique se o arquivo está no diretório correto.")
except Exception as e:
    print(f"Erro inesperado: {e}")











    