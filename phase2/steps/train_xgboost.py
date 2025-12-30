from zenml import step
from typing import Tuple
import pandas as pd
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split

@step
def train_xgboost(
    X: pd.DataFrame, 
    y: pd.Series
) -> Tuple[XGBRegressor, pd.Series, pd.Series]:
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = XGBRegressor(
        n_estimators=100,
        learning_rate=0.1,
        max_depth=5,
        random_state=42
    )
    model.fit(X_train, y_train)
    y_pred = pd.Series(model.predict(X_test), name="y_pred")
    y_test = pd.Series(y_test.values, name="y_test")

    return model, y_test, y_pred
