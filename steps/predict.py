from zenml import step
import numpy as np

@step
def predict_air_quality(model, X_test) -> float:
    prediction = model.predict(X_test.iloc[:1])
    predicted_aqi = float(prediction[0])

    print(f"Predicted AQI: {predicted_aqi}")
    return predicted_aqi
