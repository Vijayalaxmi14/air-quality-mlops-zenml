from zenml import step
from sklearn.ensemble import RandomForestRegressor
import joblib

@step
def train_model(X_train, y_train):
    """
    Trains a RandomForest model and saves it.
    """
    model = RandomForestRegressor(random_state=42)
    model.fit(X_train, y_train)
    # Save model
    joblib.dump(model, "models/rf_model.pkl")
    return model
