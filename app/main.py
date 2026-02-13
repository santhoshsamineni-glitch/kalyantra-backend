from fastapi import FastAPI

app = FastAPI(
    title="KALYANTRA API",
    description="Linear Infrastructure Planning Engine Backend",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "KALYANTRA API is running successfully 🚀"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
