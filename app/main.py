from fastapi import FastAPI
from db.session import engine
from db.base import Base

app = FastAPI(
    title="KALYANTRA API",
    description="Linear Infrastructure Planning Engine Backend",
    version="1.0.0"
)

# Create tables automatically
Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "KALYANTRA API is running successfully 🚀"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}
