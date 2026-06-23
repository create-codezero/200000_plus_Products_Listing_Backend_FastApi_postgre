from fastapi import FastAPI
from app.routes.products import router as products_router

app = FastAPI(title="Product Listing API")

app.include_router(products_router)

@app.get("/")
def root():
    return {"status": "ok"}