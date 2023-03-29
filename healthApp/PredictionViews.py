from django.shortcuts import render, redirect

import joblib
import healthApp.model_codes.breast_cancer_model as breast_cancer_model
import healthApp.model_codes.heart_model as heart_model
import healthApp.model_codes.kidney_model as kidney_model
import healthApp.model_codes.diabetes_model as diabetes_model
import healthApp.model_codes.liver_model as liver_model


def heart(request):
    return render(request, 'prediction/heart.html')


def heart_predict(request):
    if request.method == "POST":
        cp = request.POST.get('cp')
        trestbps = request.POST.get('trestbps')
        chol = request.POST.get('chol')
        fbs = request.POST.get('fbs')
        restecg = request.POST.get('restecg')
        thalach = request.POST.get('thalach')
        exang = request.POST.get('exang')

        heart_model.train_heart_model()

        loaded_model = joblib.load('training_models/heart_model.pkl')
        result = loaded_model.predict([[cp, trestbps, chol, fbs, restecg, thalach, exang]])

        if int(result[0]) == 1:
            prediction = "Bạn có thể đang có triệu chứng về bệnh tim. Hãy đến gặp bác sĩ để hiểu rõ hơn về tình trạng"
            status = 0
        else:
            prediction = "Bạn không có triệu chứng của bệnh tim"
            status = 1

        context = {
            'prediction': prediction,
            'status': status
        }
        return render(request, 'prediction/result.html', context)


def kidney(request):
    return render(request, 'prediction/kidney.html')


def kidney_predict(request):
    if request.method == "POST":
        bp = request.POST.get('bp')
        sg = request.POST.get('sg')
        al = request.POST.get('al')
        su = request.POST.get('su')
        rbc = request.POST.get('rbc')
        pc = request.POST.get('pc')
        pcc = request.POST.get('pcc')

        kidney_model.train_kidney_model()

        loaded_model = joblib.load('training_models/kidney_model.pkl')
        result = loaded_model.predict([[bp, sg, al, su, rbc, pc, pcc]])
        if int(result[0]) == 1:
            prediction = "Bạn có thể đang có triệu chứng về bệnh thận. Hãy đến gặp bác sĩ để hiểu rõ hơn về tình trạng"
            status = 0
        else:
            prediction = "Bạn không có triệu chứng của bệnh thận"
            status = 1

        context = {
            'prediction': prediction,
            'status': status
        }
        return render(request, 'prediction/result.html', context)


def diabetes(request):
    return render(request, 'prediction/diabetes.html')


def diabetes_predict(request):
    if request.method == "POST":
        Pregnancies = request.POST.get('Pregnancies')
        Glucose = request.POST.get('Glucose')
        BloodPressure = request.POST.get('BloodPressure')
        BMI = request.POST.get('BMI')
        DiabetesPedigreeFunction = request.POST.get('DiabetesPedigreeFunction')
        Age = request.POST.get('Age')
        # Outcome = request.POST.get('Outcome')

        diabetes_model.train_diabetes_model()

        loaded_model = joblib.load('training_models/diabetes_model.pkl')
        result = loaded_model.predict(
            [[Pregnancies, Glucose, BloodPressure, BMI, DiabetesPedigreeFunction, Age]])
        if int(result[0]) == 1:
            prediction = "Bạn có thể đang có triệu chứng về bệnh tiểu đường. Hãy đến gặp bác sĩ để hiểu rõ hơn về tình trạng"
            status = 0
        else:
            prediction = "Bạn không có triệu chứng của bệnh tiểu đường"
            status = 1

        context = {
            'prediction': prediction,
            'status': status
        }
        return render(request, 'prediction/result.html', context)


def liver(request):
    return render(request, 'prediction/liver.html')


def liver_predict(request):
    if request.method == "POST":
        Total_Bilirubin = request.POST.get('Total_Bilirubin')
        Direct_Bilirubin = request.POST.get('Direct_Bilirubin')
        Alkaline_Phosphotase = request.POST.get('Alkaline_Phosphotase')
        Alamine_Aminotransferase = request.POST.get('Alamine_Aminotransferase')
        Total_Protiens = request.POST.get('Total_Protiens')
        Albumin = request.POST.get('Albumin')
        Albumin_and_Globulin_Ratio = request.POST.get('Albumin_and_Globulin_Ratio')

        liver_model.train_liver_model()

        loaded_model = joblib.load('training_models/liver_model.pkl')
        result = loaded_model.predict([[Total_Bilirubin, Direct_Bilirubin, Alkaline_Phosphotase,
                                        Alamine_Aminotransferase, Total_Protiens, Albumin, Albumin_and_Globulin_Ratio]])

        if int(result[0]) == 1:
            prediction = "Bạn có thể đang có triệu chứng về bệnh gan. Hãy đến gặp bác sĩ để hiểu rõ hơn về tình trạng"
            status = 0
        else:
            prediction = "Bạn không có triệu chứng của bệnh gan"
            status = 1

        context = {
            'prediction': prediction,
            'status': status
        }
        return render(request, 'prediction/result.html', context)


def cancer(request):
    return render(request, 'prediction/cancer.html')


def cancer_predict(request):
    if request.method == "POST":
        concave_points_mean = request.POST.get('concave_points_mean')
        area_mean = request.POST.get('area_mean')
        radius_mean = request.POST.get('radius_mean')
        perimeter_mean = request.POST.get('perimeter_mean')
        concavity_mean = request.POST.get('concavity_mean')

        breast_cancer_model.train_breast_cancer_model()

        loaded_model = joblib.load('training_models/cancer_model.pkl')
        result = loaded_model.predict([[concave_points_mean, area_mean, radius_mean, perimeter_mean, concavity_mean]])
        if int(result[0]) == 1:
            prediction = "Bạn có thể đang có triệu chứng về bệnh ung thư. Hãy đến gặp bác sĩ để hiểu rõ hơn về tình trạng"
            status = 0
        else:
            prediction = "Bạn không có triệu chứng của bệnh ung thư"
            status = 1

        context = {
            'prediction': prediction,
            'status': status
        }
        return render(request, 'prediction/result.html', context)


def result(request):
    return render(request, 'prediction/result.html')