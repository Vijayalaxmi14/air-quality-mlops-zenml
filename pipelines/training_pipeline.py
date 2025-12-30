from zenml import pipeline
from steps.ingest_data import ingest_data
from steps.clean_data import clean_data
from steps.feature_selection import feature_selection
from steps.train_xgboost import train_xgboost
from steps.evaluate_model import evaluate_model
from steps.model_stub import monitor_model
from steps.alert_step import alert_system

@pipeline
def air_quality_pipeline(data_path: str):
    X, y = ingest_data(data_path)
    X, y = clean_data(X, y)
    X, y = feature_selection(X, y)
    model, y_test, y_pred = train_xgboost(X, y)
    rmse, r2 = evaluate_model(y_test, y_pred)
    avg_aqi, category = monitor_model(y_test, y_pred, rmse, r2)
    alert_system(avg_aqi, category)
