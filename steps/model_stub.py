from zenml import step
from typing import Tuple
import pandas as pd
import logging

@step
def monitor_model(y_test: pd.Series, y_pred: pd.Series, rmse: float, r2: float) -> Tuple[float, str]:
    """
    Monitor the model performance and return average AQI and category
    """
    avg_aqi = float(y_pred.mean())

    if avg_aqi <= 50:
        category = "Good"
    elif avg_aqi <= 100:
        category = "Satisfactory"
    elif avg_aqi <= 200:
        category = "Moderate"
    elif avg_aqi <= 300:
        category = "Poor"
    elif avg_aqi <= 400:
        category = "Very Poor"
    else:
        category = "Severe"

    logging.info(f"Model monitoring: RMSE={rmse:.4f}, R2={r2:.4f}")

    return avg_aqi, category
