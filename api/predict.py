from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class PredictionInput(BaseModel):
    text: str

@app.get("/")
async def root():
    return {"message": "Welcome to the Prediction API"}

@app.post("/predict")
async def predict(input_data: PredictionInput):
    # Add your prediction logic here
    return {"prediction": f"Processed: {input_data.text}"}