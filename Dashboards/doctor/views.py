from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.forms import model_to_dict
from django.http import HttpResponse, Http404
from django.urls import reverse
from django.contrib.auth.models import User
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

# from django.shortcuts import render_to_response
from patient.forms import SurveyForm
from patient.models import PatientProfile, Survey
from doctor.models import DoctorProfile

# import package for database connection
from ipdb import set_trace as debug
import sys
sys.path.append('database')   
from database.database import *
# import pycurl
from io import BytesIO
import json
import uuid
import colored_traceback.always

def home(request):
    context = {}
    doctor = request.user.doctorprofile
    patients = PatientProfile.objects.filter(doctor=doctor)
    context['patients'] = patients
    # patients: list of patient_profile object
    # Usage:
    # name: patient.user.first_name, patient.user.last_name
    # profile_picture: patient.picture

    return render(request, 'doctor/index.html', context)


def search(request):
    context = {}
    print('search now')
    if request.method != 'POST':
        print('Http404')
        raise Http404
    if not 'search_username' in request.POST or not request.POST['search_username']:
        message = 'You must enter the username of a patient.'
        json_error = '{ "error": "'+message+'" }'
        return HttpResponse(json_error, content_type='application/json')
    
    doctor = request.user.doctorprofile
    
    if 'search_username' in request.POST and request.POST['search_username'] != '':
        try:
            user = User.objects.get(username=request.POST['search_username'])
            print('print out!!!!!', user)
            search_patient = PatientProfile.objects.filter(user=user)
            print('print out!!!!!', search_patient)
            if len(search_patient) != 1:
                context['patients'] = doctor.patients.all()
                return render(request, 'doctor/index.html', context)
            else:
                print('search_patient found')
                if search_patient[0].doctor != doctor:
                    print('not correct doctor')
                    print(search_patient[0].doctor)
                    context['patients'] = doctor.patients.all()
                    return render(request, 'doctor/index.html', context)
                print('correct doctor')
                context['patients'] = search_patient
                print('return only one patient')
                return render(request, 'doctor/index.html', context)
        except:
            print('try fail')
            context['patients'] = doctor.patients.all()
    else:
        print('no request post')
        context['patients'] = doctor.patients.all()
    return render(request, 'doctor/index.html', context)

def add_patient(request):
    context = {}
    print("100")
    if request.method != 'POST':
        print ("404")
        raise Http404
    if not 'search_username' in request.POST or not request.POST['search_username']:
        message = 'You must enter the username of a patient.'
        json_error = '{ "error": "'+message+'" }'
        return HttpResponse(json_error, content_type='application/json')
    
    input_username = request.POST['search_username']
    print(input_username)
    patient_user = User.objects.filter(username=input_username)
    patient = patient_user[0].patientprofile
    doctor = request.user.doctorprofile
    # ignore already added ones
    if not patient.doctor is doctor :
        patient.doctor = doctor
        patient.save()

    context['patients'] = doctor.patients.all()
    print(doctor.patients.all())
    return render(request, 'doctor/index.html', context)

def todo(request):
    return render(request, 'doctor/todo.html')


def calendar(request):
    return render(request, 'doctor/calendar.html')


def metrics(request):
    return render(request, 'doctor/metrics.html')


def exercises(request):
    return render(request, 'doctor/exercises.html')


def survey(request):
    return render(request, 'doctor/survey.html')


def register(request):
    return render(request, 'doctor/register.html')


def login(request):
    return render(request, 'doctor/login.html')


def view_details(request, username):
    context = {}
    patient_user = User.objects.filter(username=username)
    context['patient'] = patient_user[0].patientprofile
    return render(request, 'doctor/view_details.html', context)


def patient_info(request, username):
    context = {}
    patient_user = User.objects.filter(username=username)
    context['patient']= patient_user[0].patientprofile
    return render(request, 'doctor/patient_info.html', context)


def questionnaire(request, username):
    context = {}
    patient_user = User.objects.filter(username=username)
    context['patient'] = patient_user[0].patientprofile
    context['form'] = patient_user[0].patientprofile.survey
    if patient_user[0].patientprofile.survey is None:
        object = SurveyForm()
    else: 
        object = SurveyForm(data=model_to_dict(
        Survey.objects.get(pk=patient_user[0].patientprofile.survey.id)))
    return render(request, 'doctor/questionnaire.html', {'form': object, 'patient': patient_user[0].patientprofile})


def profile(request):
    return render(request, 'doctor/profile.html')


def set_questionnaire(request, username):
    context = {}
    patient_user = User.objects.filter(username=username)
    context['patient'] = patient_user[0].patientprofile
    return render(request, 'doctor/set_questionnaire.html', context)


@login_required
@csrf_exempt
def metric_display(request):
    db = get_db()
    patient_id = request.POST['username']
    print(patient_id)
    patient_id = '10000000-0000-0000-0000-000000000000'

    diction = {}
    # 1. mood
    retrieved_emotion = find_emotion_by_patient_id(db, patient_id)
    print("fetch emotion")

    # truncate emotion length to 30 days
    if len(retrieved_emotion) > 30:
        retrieved_emotion = retrieved_emotion[len(
            retrieved_emotion) - 30: len(retrieved_emotion)]

    # init mood dict
    diction["mood"] = {"time": ["0000-00-00"] * 30, "yvalue": {}}
    diction["mood"]["yvalue"] = {"neutral": [0] * 30, "happiness": [0] * 30,
                                 "sadness": [0] * 30, "surprise": [0] * 30, "anger": [0] * 30}
    index = 0

    # fill in the dictionary
    for row in retrieved_emotion:
        while (index < 30 - len(retrieved_emotion)):
            index = index + 1
        print(index)
        time = row["created_at"].strftime("%Y-%m-%d")
        neutral = str(row["neutral"] * 100)
        happiness = str(row["happiness"] * 100)
        sadness = str(row["sadness"] * 100)
        surprise = str(row["surprise"] * 100)
        anger = str(row["anger"] * 100)

        diction["mood"]["time"][index] = time
        diction["mood"]["yvalue"]["neutral"][index] = neutral
        diction["mood"]["yvalue"]["happiness"][index] = happiness
        diction["mood"]["yvalue"]["sadness"][index] = sadness
        diction["mood"]["yvalue"]["surprise"][index] = surprise
        diction["mood"]["yvalue"]["anger"][index] = anger
        index = index + 1

    print(diction["mood"])
    print("==================================================================")

    # 2. game
    # Issue: a) Only one game for now

    retrieved_game = find_game_by_patient_id(db, patient_id)

    # truncate game length to 30 days
    if len(retrieved_game) > 30:
        retrieved_game = retrieved_game[len(
            retrieved_game) - 30: len(retrieved_game)]
    print(retrieved_game)

    # init game dict
    diction["game"] = {"time": {}, "yvalue": {}}
    diction["game"]["time"] = {"game1_time": [
        "0000-00-00"] * 30, "game2_time": ["0000-00-00"] * 30, "game3_time": ["0000-00-00"] * 30}
    diction["game"]["yvalue"] = {"WordSearch": [
        0] * 30, "TileMatching": [0] * 30, "BrownPeterson": [0] * 30}
    #

    index = 0

    # fill in the dictionary
    for row in retrieved_game:

        while (index < 30 - len(retrieved_game)):
            index = index + 1
        print(index)
        time = row["created_at"].strftime("%Y-%m-%d")
        left = row["left_hand_score"]
        right = row["right_hand_score"]

        diction["game"]["time"]["game1_time"][index] = time
        diction["game"]["yvalue"]["WordSearch"][index] = (left + right) / 2
        index = index + 1

    print(diction["game"])
    print("==================================================================")

    # Biometric:
    # Issue: a) currenlty no tremor data
    #        b) blood pressure is not systolic + diastolic: only one value
    retrieved_biometric = find_biometric_by_patient_id(db, patient_id)
    # print(len(retrieved_biometric))
    # print(retrieved_biometric)
    # truncate emotion length to 30 days
    if len(retrieved_biometric) > 30:
        retrieved_biometric = retrieved_biometric[len(
            retrieved_biometric) - 30: len(retrieved_biometric)]

    # 3. blood
    diction["blood"] = {"time": ["0000-00-00"] * 30, "yvalue": {}}
    diction["blood"]["yvalue"] = {"systolic": [0] * 30, "diastolic": [0] * 30}

    # 4. heartrate
    diction["heartrate"] = {"time": ["0000-00-00"] * 30, "yvalue": [0] * 30}

    # 5. tremor1
    diction["tremor1"] = {"time": ["0000-00-00"] * 30, "yvalue": [0] * 30}

    # 6. tremor2
    diction["tremor2"] = {"time": ["0000-00-00"] * 30, "yvalue": [0] * 30}

    index = 0
    # fill in the dictionary
    for row in retrieved_biometric:
        while (index < 30 - len(retrieved_biometric)):
            index = index + 1

        print(index)
        time = row["created_at"].strftime("%Y-%m-%d")
        blood = str(row["blood_pressure"])
        systolic = blood
        diastolic = blood

        heartrate_value = str(row["heart_rate"])
        # tremor1_value = feature["tremor1"]
        # tremor2_value = feature["tremor2"]

        diction["blood"]["time"][index] = time
        diction["blood"]["yvalue"]["systolic"][index] = systolic
        diction["blood"]["yvalue"]["diastolic"][index] = diastolic

        diction["heartrate"]["time"][index] = time
        diction["heartrate"]["yvalue"][index] = heartrate_value

        # diction["tremor1"]["time"][index] = time
        # diction["tremor1"]["yvalue"][index] = tremor1_value

        # diction["tremor2"]["time"][index] = time
        # diction["tremor2"]["yvalue"][index] = tremor2_value

        index = index + 1

    print(diction["blood"])
    print("==================================================================")

    print(diction["heartrate"])
    print("==================================================================")

    return HttpResponse(json.dumps(diction), content_type='application/json')

@login_required
@csrf_exempt
def view_general(request):
    db = get_db()
    patient_id = request.POST['username']
    print(patient_id)
    patient_id = '10000000-0000-0000-0000-000000000000'

    diction = {}
    # 1. mood
    retrieved_emotion = find_emotion_by_patient_id(db, patient_id)
    print("fetch emotion")

    # truncate emotion length to 30 days

    # init mood dict
    diction["mood"] = {"time": "0000-00-00", "yvalue": []}
    # diction["mood"]["yvalue"] = []

    # fill in the dictionary
    if len(retrieved_emotion) >= 1:
        time = retrieved_emotion[-1]["created_at"].strftime("%Y-%m-%d")
        neutral = str(retrieved_emotion[-1]["neutral"] * 100)
        happiness = str(retrieved_emotion[-1]["happiness"] * 100)
        sadness = str(retrieved_emotion[-1]["sadness"] * 100)
        surprise = str(retrieved_emotion[-1]["surprise"] * 100)
        anger = str(retrieved_emotion[-1]["anger"] * 100)

        diction["mood"]["time"] = time
        diction["mood"]["yvalue"].append(neutral)
        diction["mood"]["yvalue"].append(happiness)
        diction["mood"]["yvalue"].append(sadness)
        diction["mood"]["yvalue"].append(surprise)
        diction["mood"]["yvalue"].append(anger)

    print(diction["mood"])
    print("==================================================================")

    return HttpResponse(json.dumps(diction), content_type='application/json')
