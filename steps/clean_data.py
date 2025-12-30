from zenml import step
import pandas as pd
from typing import Tuple

@step
def clean_data(X: pd.DataFrame, y: pd.Series) -> Tuple[pd.DataFrame, pd.Series]:
    """
    Cleans dataset: fills missing values and ensures numeric types.
    """
    df = X.copy()
    df["AQI"] = y

    required_cols = ["PM2.5", "PM10", "CO", "O3", "AQI"]
    df = df[required_cols]

    for col in required_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df = df.dropna(subset=["AQI"])
    for col in ["PM2.5", "PM10", "CO", "O3"]:
        df[col] = df[col].fillna(df[col].mean())

    X_clean = df.drop("AQI", axis=1)
    y_clean = df["AQI"]

    # Save cleaned data locally for DVC tracking
    X_clean.assign(AQI=y_clean).to_csv("data/processed/clean_data.csv", index=False)

    return X_clean, y_clean
