import numpy as np
import pandas as pd
from sklearn import ensemble
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib


def train_heart_model():
    df = pd.read_csv("data/heart.csv")

    categorical_val = []
    continuous_val = []
    for column in df.columns:
        if len(df[column].unique()) <= 10:
            categorical_val.append(column)
        else:
            continuous_val.append(column)

    categorical_val.remove('target')
    dataset = pd.get_dummies(df, columns=categorical_val)

    cols = ['cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang']
    x = df[cols]
    y = dataset.target

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)
    print('Shape training set: X:{}, y:{}'.format(x_train.shape, y_train.shape))
    print('Shape test set: X:{}, y:{}'.format(x_test.shape, y_test.shape))

    model = ensemble.RandomForestClassifier()
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    print('Accuracy : {}'.format(accuracy_score(y_test, y_pred)))

    clf_report = classification_report(y_test, y_pred)
    print('Classification report')
    print("---------------------")
    print(clf_report)
    print("_____________________")

    joblib.dump(model, r"C:\Users\Lenovo\PycharmProjects\ehealthy\training_models\heart_model.pkl")
