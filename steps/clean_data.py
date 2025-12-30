from zenml import step
import pandas as pd
from typing import Tuple

@step
def clean_data(X: pd.DataFrame, y: pd.Series) -> Tuple[pd.DataFrame, pd.Series]:
    df = X.copy()
    df["AQI"] = y

    required_cols = ["PM2.5", "PM10", "CO", "O3", "AQI"]
    df = df[required_cols]

    # Convert to numeric safely
    for col in required_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Drop rows where AQI is missing
    df = df.dropna(subset=["AQI"])

    # Fill missing pollutant values
    for col in ["PM2.5", "PM10", "CO", "O3"]:
        df[col] = df[col].fillna(df[col].mean())

    X_clean = df.drop("AQI", axis=1)
    y_clean = df["AQI"]

    return X_clean, y_clean
