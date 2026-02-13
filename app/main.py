from fastapi import FastAPI
from sqlalchemy import create_engine, text
import os

app = FastAPI(
    title="KALYANTRA API",
    description="Linear Infrastructure Planning Engine Backend",
    version="1.0.0"
)

# 🔹 Database connection
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)


@app.get("/")
def root():
    return {"message": "KALYANTRA API is running successfully 🚀"}


@app.get("/health")
def health_check():
