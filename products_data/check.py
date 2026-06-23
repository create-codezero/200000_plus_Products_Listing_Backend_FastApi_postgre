import pandas as pd

df = pd.read_csv("./products_data/products.csv")

print(df.shape)
print(df.head())

print(df["category"].nunique())
print(df["brand"].nunique())

print(df["price"].min())
print(df["price"].max())