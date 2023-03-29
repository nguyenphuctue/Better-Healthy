import numpy as np
import pandas as pd
from sklearn import ensemble
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib


def train_breast_cancer_model():
    df = pd.read_csv(r"data/cancer.csv")
    df.drop(df.columns[[0, -1]], axis=1, inplace=True)
    # Split the features data and the target
    x_data = df.drop(['diagnosis'], axis=1)
    y_data = df['diagnosis']

    # Encoding the target value
    yenc = np.asarray([1 if c == 'M' else 0 for c in y_data])
    cols = ['concave points_mean', 'area_mean', 'radius_mean', 'perimeter_mean', 'concavity_mean']
    x_data = df[cols]
    print(x_data.head())

    x_train, x_test, y_train, y_test = train_test_split(x_data, yenc, test_size=0.3, random_state=43)
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

    joblib.dump(model, r"training_models/cancer_model.pkl")
