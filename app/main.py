from fastapi import FastAPI
from sqlalchemy import text
from db.session import engine
from db.base import Base
from sqlalchemy.orm import Session
from db.session import SessionLocal
from models.organization import Organization

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
@app.get("/organizations")
def get_organizations():
    db: Session = SessionLocal()
    try:
        organizations = db.query(Organization).all()
        return organizations
    finally:
        db.close()
    
