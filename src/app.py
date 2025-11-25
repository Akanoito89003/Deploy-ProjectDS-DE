from fastapi import FastAPI
from pydantic import BaseModel
import os

app = FastAPI(
    title="THB Forecast API",
    description="API for forecasting THB/USD exchange rates",
    version="1.0.0"
)

class PredictionRequest(BaseModel):
    # Define your input schema here
    # Example:
    # date: str
    pass

@app.get("/")
def read_root():
    return {"message": "Welcome to THB Forecast API. Go to /docs for API documentation."}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/predict")
def predict(request: PredictionRequest):
    # Placeholder for prediction logic
    # You would load your model here or globally and use it to predict
    return {"prediction": "Not implemented yet", "input": request.dict()}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=10000)
