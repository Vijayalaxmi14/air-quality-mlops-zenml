from zenml import pipeline
from steps.ingest import ingest_data
from steps.clean import clean_data
from steps.preprocess import preprocess_data
from steps.feature_selection import feature_selection
from steps.train_model import train_model
from steps.alert_system import alert_system
import pandas as pd

@pipeline
def aqi_pipeline():
    # ingest data
    X, y = ingest_data()

    # clean
    X_clean, y_clean = clean_data(X, y)

    # feature selection
    X_sel, y_sel = feature_selection(X_clean, y_clean)

    # preprocessing (train/test split)
    X_train, X_test, y_train, y_test = preprocess_data(X_sel, y_sel)

    # train model
    model = train_model(X_train, y_train)

    # simple alert (example: mean AQI)
    avg_aqi = y.mean()
    category = "Unhealthy" if avg_aqi > 200 else "Good"
    alert_system(avg_aqi, category)


if __name__ == "__main__":
    pipeline = aqi_pipeline()
    pipeline.run()
