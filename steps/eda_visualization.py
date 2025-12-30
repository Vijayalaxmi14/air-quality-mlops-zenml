from zenml import step
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

@step
def eda_visualization(X: pd.DataFrame, y):
    # 1️⃣ Feature Distribution
    plt.figure(figsize=(8,5))
    X.iloc[:, :5].hist()
    plt.suptitle("Feature Distribution")
    plt.tight_layout()
    plt.show()

    # 2️⃣ Correlation Heatmap
    plt.figure(figsize=(10,6))
    sns.heatmap(X.corr(), cmap="coolwarm")
    plt.title("Feature Correlation Heatmap")
    plt.show()

    # 3️⃣ Target Distribution
    plt.figure(figsize=(6,4))
    y.value_counts().plot(kind="bar")
    plt.title("Target Variable Distribution")
    plt.show()
