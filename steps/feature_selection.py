from zenml import step
from typing import Tuple
import pandas as pd

@step
def feature_selection(X: pd.DataFrame, y: pd.Series) -> Tuple[pd.DataFrame, pd.Series]:
    """
    Placeholder for feature selection logic.
    Returns the same features and target for now.
    """
    return X, y
