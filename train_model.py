import pandas as pd
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
import mlflow
import mlflow.sklearn


def train():
    # 1. Load Data
    print("Loading data...")
    data = load_wine()
    X = pd.DataFrame(data.data, columns=data.feature_names)
    y = data.target

    # 2. Split Data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # 3. Train Model & Log to MLflow
    print("Training model...")
    mlflow.set_experiment("wine-quality-experiment")
    
    with mlflow.start_run():
        n_estimators = 10
        random_state = 42
        
        # Log parameters
        mlflow.log_param("n_estimators", n_estimators)
        mlflow.log_param("random_state", random_state)
        
        model = RandomForestClassifier(n_estimators=n_estimators, random_state=random_state)
        model.fit(X_train, y_train)

        # 4. Evaluate
        predictions = model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        print(f"Model Accuracy: {accuracy:.2f}")
        
        # Log metrics
        mlflow.log_metric("accuracy", accuracy)

        # 5. Save Model
        print("Saving model to model.joblib...")
        joblib.dump(model, "model.joblib")
        
        # Log model artifact
        mlflow.sklearn.log_model(model, "model")
        print("Done!")


if __name__ == "__main__":
    train()
