from zenml import step
import pandas as pd
from typing import Tuple
import dvc.api

@step
def ingest_data() -> Tuple[pd.DataFrame, pd.Series]:
    """
    Reads DVC-tracked CSV and returns features and target.
    """
    data_url = dvc.api.get_url(
        path="data/raw/city_hour.csv",
        repo="."
    )
    df = pd.read_csv(data_url)
    X = df.drop("AQI", axis=1)
    y = df["AQI"]
    return X, y
