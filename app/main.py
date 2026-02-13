from fastapi import FastAPI
from sqlalchemy import text
from db.session import engine
from db.base import Base

app = FastAPI(
    title="KALYANTRA API",
    description="Linear Infrastructure Planning Engine Backend",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "KALYANTRA API is running successfully 🚀"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/db-check")
def db_check():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        return {"database_status": "connected"}
    except Exception as e:
        return {"database_status": "error", "details": str(e)}
