from zenml import step
import logging

@step
def monitor_model(metrics: tuple[float, float]):
    rmse, r2 = metrics
    logging.info(f"Model monitoring: RMSE={rmse:.4f}, R2={r2:.4f}")
