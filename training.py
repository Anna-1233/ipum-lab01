import joblib
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split


def load_data():
    iris = load_iris()
    X, y = iris.data, iris.target
    return train_test_split(X, y, test_size=0.2, random_state=42)


def train_model(X_train, y_train):
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('classifier', LogisticRegression(random_state=42, max_iter=200))
    ])

    pipeline.fit(X_train, y_train)
    return pipeline


def save_model(model, file="model.joblib"):
    joblib.dump(model, file)


if __name__ == '__main__':
    X_train, X_test, y_train, y_test = load_data()
    model = train_model(X_train, y_train)
    save_model(model)



