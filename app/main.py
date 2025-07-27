
from fastapi import FastAPI
from app.model import predict
from app.schemas import PredictRequest, PredictResponse

app = FastAPI()

@app.post("/predict", response_model=PredictResponse)
def predict_endpoint(req: PredictRequest):
    prediction = predict(req.features)
    return PredictResponse(prediction=prediction)
