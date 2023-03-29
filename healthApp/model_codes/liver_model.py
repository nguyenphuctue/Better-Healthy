import numpy as np
import pandas as pd
from sklearn import ensemble
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib


def train_liver_model():
    patients = pd.read_csv('data/indian_liver_patient.csv')
    patients['Gender'] = patients['Gender'].apply(lambda x: 1 if x == 'Male' else 0)
    patients = patients.fillna(0.94)

    x = patients[['Total_Bilirubin', 'Direct_Bilirubin',
                  'Alkaline_Phosphotase', 'Alamine_Aminotransferase',
                  'Total_Protiens', 'Albumin', 'Albumin_and_Globulin_Ratio']]
    y = patients['Dataset']

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=123)

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

    joblib.dump(model, r"C:\Users\Lenovo\PycharmProjects\ehealthy\training_models\liver_model.pkl")
