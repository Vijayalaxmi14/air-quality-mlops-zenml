from zenml import step
import pandas as pd
from typing import Tuple

@step
def ingest_data(data_path: str) -> Tuple[pd.DataFrame, pd.Series]:
    """
    Reads CSV and returns features and target
    """
    df = pd.read_csv(data_path)
    X = df.drop("AQI", axis=1)
    y = df["AQI"]
    return X, y
