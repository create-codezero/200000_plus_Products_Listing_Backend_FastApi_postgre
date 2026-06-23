import pandas as pd

df = pd.read_csv("./products_data/products.csv")

print(
    df.groupby("updated_at")
      .size()
      .sort_values(ascending=False)
      .head(10)
)