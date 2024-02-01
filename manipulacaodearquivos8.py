#PACOTE PANDAS
import pandas as pd

arquivo = "arquivos/salarios.csv"

df = pd.read_csv(arquivo)

print(df.head())

print(df['Position Title'].value_counts())