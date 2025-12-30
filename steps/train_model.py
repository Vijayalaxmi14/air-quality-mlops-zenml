from zenml import step
from sklearn.ensemble import RandomForestRegressor

@step
def train_model(X_train, y_train):
    model = RandomForestRegressor(random_state=42)
    model.fit(X_train, y_train)
    return model
