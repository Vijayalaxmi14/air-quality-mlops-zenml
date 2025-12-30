from zenml import pipeline
from steps.ingest_data import ingest_data
from steps.preprocess import preprocess_data
from steps.eda_visualization import eda_visualization
from steps.train import train_model
from steps.evaluate import evaluate_model
from steps.alert import alert_system

@pipeline
def model_pipeline():
    X, y = ingest_data()
    
    eda_visualization(X, y)   # 👈 EDA shown in dashboard
    
    X_p, y_p = preprocess_data(X, y)
    model = train_model(X_p, y_p)
    accuracy = evaluate_model(model, X_p, y_p)
    alert = alert_system(accuracy)
    
    return alert
