import pandas as pd

df = pd.read_excel("data/raw/bangalore.xlsx")
df = df.dropna()
df.to_csv("data/processed/clean_data.csv", index=False)
