import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL, pool_pre_ping=True)

CSV_PATH = "../products_data/products.csv"


def chunked_insert(df, table_name="products"):
    df.to_sql(
        table_name,
        engine,
        if_exists="append",
        index=False,
        chunksize=5000,
        method="multi"
    )


def main():
    print("Reading CSV...")

    df = pd.read_csv(CSV_PATH)

    print("Total rows:", len(df))

    # -----------------------------
    # Normalize column names FIRST
    # -----------------------------
    df.columns = [c.lower() for c in df.columns]

    # -----------------------------
    # Validate required columns
    # -----------------------------
    required_cols = ["public_id", "name", "updated_at", "created_at"]
    for col in required_cols:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")

    # -----------------------------
    # FIX: Convert timestamps (CRITICAL)
    # -----------------------------
    df["created_at"] = pd.to_datetime(df["created_at"], errors="coerce")
    df["updated_at"] = pd.to_datetime(df["updated_at"], errors="coerce")

    # Drop invalid rows after conversion
    df = df.dropna(subset=["public_id", "name", "updated_at", "created_at"])

    print("Clean rows:", len(df))

    print("Starting import...")

    chunk_size = 20000

    for i in range(0, len(df), chunk_size):
        chunk = df.iloc[i:i + chunk_size]

        chunked_insert(chunk)

        print(f"Inserted: {min(i + chunk_size, len(df))}/{len(df)}")

    print("DONE ✔")


if __name__ == "__main__":
    main()