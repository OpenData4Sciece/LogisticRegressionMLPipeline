
import joblib
import numpy as np
from pathlib import Path

model_path = Path(__file__).parent.parent / "models" / "logistic_model.joblib"
model = joblib.load(model_path)

def predict(features: list) -> int:
    X = np.array(features).reshape(1, -1)
    return int(model.predict(X)[0])
