from zenml import step

@step
def alert_system(metrics):
    """
    Example alert system.
    """
    rmse, r2 = metrics
    if rmse > 50:
        print(f"⚠️ Alert! RMSE is high: {rmse:.2f}")
    else:
        print(f"✅ Metrics are OK: RMSE={rmse:.2f}, R2={r2:.2f}")
from zenml import step
import logging

@step
def alert_system(avg_aqi: float, category: str):
    if avg_aqi > 200:
        print(f"⚠️ ALERT! AQI is {avg_aqi:.2f} ({category})")
    else:
        print(f"✅ AQI is OK: {avg_aqi:.2f} ({category})")
