from fastapi import FastAPI
from app.routes.products import router as products_router

app = FastAPI(title="Product Listing API")

app.include_router(products_router)

@app.get("/")
def root():
    return {"status": "ok"}

import os
from sqlalchemy import text
from app.db import engine

@app.get("/debug-db")
def debug_db():
    with engine.connect() as conn:
        db_name = conn.execute(text("SELECT current_database()")).scalar()
        schema_name = conn.execute(text("SELECT current_schema()")).scalar()

        tables = conn.execute(text("""
            SELECT table_name
            FROM information_schema.tables
            WHERE table_schema = 'public'
        """)).fetchall()

        return {
            "database": db_name,
            "schema": schema_name,
            "tables": [t[0] for t in tables]
        }
