from zenml import step
from typing import Tuple
import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

@step
def evaluate_model(y_test: pd.Series, y_pred: pd.Series) -> Tuple[float, float]:
    """
    Evaluates model performance.
    Returns RMSE and R2 score.
    """
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2 = r2_score(y_test, y_pred)
    return rmse, r2
