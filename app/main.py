import os
from fastapi import FastAPI
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="KALYANTRA API",
    description="Linear Infrastructure Planning Engine Backend",
    version="1.0.0"
)

DATABASE_URL = os.getenv("DATABASE_URL")

@app.get("/")
def root():
    return {"message": "KALYANTRA API is running successfully 🚀"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/db-check")
def db_check():
    try:
        engine = create_engine(DATABASE_URL)
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        return {"database_status": "connected"}
    except Exception as e:
        return {"database_status": "error", "details": str(e)}
