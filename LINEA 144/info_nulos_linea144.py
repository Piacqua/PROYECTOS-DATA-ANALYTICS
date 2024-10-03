import pandas as pd

df = pd.read_csv("db_Linea144.csv", encoding="latin-1")

df.info()
print()
print(df.isna().sum().sort_values(ascending=False))
