from zenml import step
from sklearn.model_selection import train_test_split

@step
def preprocess_data(X, y):
    """
    Splits data into train and test sets.
    """
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    return X_train, X_test, y_train, y_test
