from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.forms import model_to_dict
from django.http import HttpResponse, Http404
from django.urls import reverse
from django.contrib.auth.models import User
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import datetime
# from django.shortcuts import render_to_response
from patient.forms import SurveyForm
from doctor.forms import DoctorCalendarEventForm
from caregiver.forms import CalendarEventForm
from patient.models import PatientProfile, Survey, CalendarEvent, SurveySetting
from doctor.models import DoctorProfile, DoctorCalendarEvent
from django.contrib import messages
from .forms import SurveySettingForm
from django import forms
# create JSON objects (used for calendar events)
from django.core import serializers
import json


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

user_dict = {}
user_dict[1] = '0c9ccfdc-833b-11ea-bc55-0242ac130003'
user_dict[2] = '0c9cd270-833b-11ea-bc55-0242ac130003'
user_dict[3] = '0c9cd50e-833b-11ea-bc55-0242ac130003'
user_dict[4] = '0c9cd608-833b-11ea-bc55-0242ac130003'

game_dict = {}
game_dict['d478236ca3614ba58a7001a1288c1bb4'] = 'Beatbox_Easy'
game_dict['da62200a344544e0831d8a2e20178bb8'] = 'Beatbox_Medium'
game_dict['155c3086583c46adafcc782a66255e73'] = 'Beatbox_Hard'
game_dict['e9d2684af30c400282fca40fde00d8f3'] = 'TwistFit_Easy'
game_dict['6a9df26a8f51457c9972cbe9b0828a86'] = 'Twistfit_Medium'
game_dict['1'] = 'WordSearch'
game_dict['2'] = 'TileMatching'
game_dict['3'] = 'BrownPeterson'

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

    doctor = request.user.doctorprofile
    if not 'search_username' in request.POST or not request.POST['search_username']:
        # message = 'You must enter the username of a patient.'
        # json_error = '{ "error": "'+message+'" }'
        # return HttpResponse(json_error, content_type='application/json')
    
        message = 'You must enter a valid username of a patient.'
        return render(request, 'doctor/index.html', {'search_alert_flag': True, 'patients': doctor.patients.all()})

    
    
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
            return render(request, 'doctor/index.html', {'search_alert_flag': True, 'patients': doctor.patients.all()})
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

    doctor = request.user.doctorprofile
    if not 'search_username' in request.POST or not request.POST['search_username']:
        # message = 'You must enter a valid username of a patient.'

        # json_error = '{ "error": "'+message+'" }'
        # return HttpResponse(json_error, content_type='application/json')
        return render(request, 'doctor/index.html', {'alert_flag': True, 'patients': doctor.patients.all()})

    try:
        input_username = request.POST['search_username']
        print(input_username)
        patient_user = User.objects.filter(username=input_username)
        patient = patient_user[0].patientprofile
        
        # ignore already added ones
        if not patient.doctor is doctor :
            patient.doctor = doctor
            patient.save()

        context['patients'] = doctor.patients.all()
        print(doctor.patients.all())
    except:
        print('try fail')
        return render(request, 'doctor/index.html', {'alert_flag': True, 'patients': doctor.patients.all()})

    return render(request, 'doctor/index.html', context)

def todo(request):
    return render(request, 'doctor/todo.html')


def calendar(request):
    if request.method == 'POST':
        form = DoctorCalendarEventForm(request.POST)
        if form.is_valid():
            description = form.cleaned_data['description']
            date = form.cleaned_data['date']
            start = form.cleaned_data['start_time']
            end = form.cleaned_data['end_time']
            patient_id = form.cleaned_data['patient']

            # add to doctor
            doctor = request.user.doctorprofile
            newevent = DoctorCalendarEvent(doctor=doctor, description=description, date=date, start=start, end=end)
            newevent.save()

            # add to patient
            patient = User.objects.get(username=patient_id)
            if (patient):
                patient = patient.patientprofile
                print("patient name is: " + patient.user.username)
                newevent = CalendarEvent(patient=patient, description=description, date=date, start=start, end=end)
                newevent.save()
            return redirect("/doctor/calendar")

    form = DoctorCalendarEventForm()
    context = {'form': form}
    return render(request, 'doctor/calendar.html', context)


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

def games(request, username):
    context = {}
    patient_user = User.objects.filter(username=username)
    context['patient'] = patient_user[0].patientprofile
    return render(request, 'doctor/game_record.html', context)

def patient_info(request, username):
    print("here")
    db = get_db()
    context = {}
    patient_user = User.objects.filter(username=username)
    patient = patient_user[0].patientprofile
    context['patient'] = patient
    survey = patient.survey
    surveySetting = patient.surveySetting
    if survey is None:
        context['exist_alert'] = 0
    else:
        
        fields = []
        for key, value in survey.__dict__.items():
            print(key, '  =>  ', value)
            if surveySetting.__dict__[key] is True and value == 5:
                fields.append(key)
        context['alert_fields'] = fields
        if len(fields) >= 4:
            context['exist_alert'] = 2
            context['alert_fields'] = fields[0:3]
            context['count'] = len(fields) - 3
        elif len(fields) == 0:
            context['exist_alert'] = 0
        else:
            context['exist_alert'] = 1
            context['count'] = len(fields)
        print(fields)

    patient_id = user_dict[patient.user.id]
    print(patient_id)

    # 1. mood
    retrieved_biometric = find_biometric_by_patient_id(db, patient_id)

    if len(retrieved_biometric) >= 1:
        heart_rate = str(retrieved_biometric[-1]["heart_rate"])
        diastolic = str(retrieved_biometric[-1]["dbp"])
        systolic = str(retrieved_biometric[-1]["sbp"])
        # tremor1 = str(retrieved_biometric[-1]["tremor1"])
        # tremor2 = str(retrieved_biometric[-1]["tremor2"])
        context['heartrate'] = heart_rate
        context['blood'] = diastolic + '/' + systolic
        context['tremor1'] = '2'
        context['tremor2'] = '3'
    else:
        context['heartrate'] = '0'
        context['blood'] = '0/0'
        context['tremor1'] = '0'
        context['tremor2'] = '0'
    return render(request, 'doctor/patient_info.html', context)


def questionnaire(request, username):
    context = {}
    patient_user = User.objects.filter(username=username)
    patient = patient_user[0].patientprofile
    context['patient'] = patient
    if patient_user[0].patientprofile.survey is None:
        form = SurveyForm()
        print("no form")
        return render(request, 'doctor/questionnaire.html', {'form': form, 'patient': patient_user[0].patientprofile, 'no_form': True})
    else:
        form = SurveyForm(data=model_to_dict(
            Survey.objects.get(pk=patient_user[0].patientprofile.survey.id)))
    
    
    for key, value in patient.surveySetting.__dict__.items():
        # if key == "csrfmiddlewaretoken":
        #     continue
        print(key, '  =>  ', value)
        if key == 'falls':
            if value == False:
                form.fields['falls'].widget = forms.HiddenInput()

        if key == 'depression':
            if value == False:
                form.fields['depression'].widget = forms.HiddenInput()

        if key == 'dyskinesia':
            if value == False:
                form.fields['dyskinesia'].widget = forms.HiddenInput()

        if key == 'movement':
            if value == False:
                form.fields['movement'].widget = forms.HiddenInput()

        if key == 'thinking':
            if value == False:
                form.fields['thinking'].widget = forms.HiddenInput()

        if key == 'walking':
            if value == False:
                form.fields['walking'].widget = forms.HiddenInput()

        if key == 'chest_pain':
            if value == False:
                form.fields['chest_pain'].widget = forms.HiddenInput()

        if key == 'tremor':
            if value == False:
                form.fields['tremor'].widget = forms.HiddenInput()

        if key == 'swallowing':
            if value == False:
                form.fields['swallowing'].widget = forms.HiddenInput()

        if key == 'pain':
            if value == False:
                form.fields['pain'].widget = forms.HiddenInput()

        if key == 'anxiety':
            if value == False:
                form.fields['anxiety'].widget = forms.HiddenInput()

        if key == 'seizures':
            if value == False:
                form.fields['seizures'].widget = forms.HiddenInput()

        if key == 'rigidity':
            if value == False:
                form.fields['rigidity'].widget = forms.HiddenInput()

        if key == 'motivation':
            if value == False:
                form.fields['motivation'].widget = forms.HiddenInput()

        if key == 'sleep':
            if value == False:
                form.fields['sleep'].widget = forms.HiddenInput()

        if key == 'muscle_spasm':
            if value == False:
                form.fields['muscle_spasm'].widget = forms.HiddenInput()

        if key == 'fatigue':
            if value == False:
                form.fields['fatigue'].widget = forms.HiddenInput()

        if key == 'hallucinations':
            if value == False:
                form.fields['hallucinations'].widget = forms.HiddenInput()

        if key == 'constipation':
            if value == False:
                form.fields['constipation'].widget = forms.HiddenInput()
    
    context['form'] = form
    print("has form")
    return render(request, 'doctor/questionnaire.html', {'form': form, 'patient': patient_user[0].patientprofile, 'no_form': False})


def profile(request):
    return render(request, 'doctor/profile.html')

def set_questionnaire(request, username):
    context = {}
    patient_user = User.objects.filter(username=username)
    context['patient'] = patient_user[0].patientprofile
    if request.method == 'GET':
        if patient_user[0].patientprofile.surveySetting is None:
            object = SurveySettingForm()
        else:
            object = SurveySettingForm(data=model_to_dict(
                SurveySetting.objects.get(pk=patient_user[0].patientprofile.surveySetting.id)))
        context['form'] = object
        return render(request, 'doctor/set_questionnaire.html', context)

    # # if patient_user[0].patientprofile.surveySetting is None:
    # #     object = SurveySettingForm()
    # # else:
    # #     object = SurveySettingForm(data=model_to_dict(
    # #         SurveySetting.objects.get(pk=patient_user[0].patientprofile.surveySetting.id)))
    # # context['form'] = object


    # # Just display the registration form if this is a GET request.
    # if request.method == 'GET':
    #     context['form'] = SurveySettingForm()
    #     return render(request, 'doctor/set_questionnaire.html', context)

    form = SurveySettingForm(request.POST)
    context['form'] = form

    if not request.user.is_authenticated:
        print("user is not authenticated")
        return render(request, 'doctor/set_questionnaire.html', context)

    patient_user = User.objects.filter(username=username)
    patient = patient_user[0].patientprofile
    
    print(patient.surveySetting)
    surveySetting = patient.surveySetting
    if 'falls' not in request.POST:
        return render(request, 'doctor/set_questionnaire.html', context)

    for key in request.POST:
        if key == "csrfmiddlewaretoken":
            continue
        value = request.POST[key]

        if key == 'falls':
            surveySetting.falls = value
        if key == 'depression':
            surveySetting.depression = value
        if key == 'dyskinesia':
            surveySetting.dyskinesia = value
        if key == 'movement':
            surveySetting.movement = value
        if key == 'thinking':
            surveySetting.thinking = value
        if key == 'walking':
            surveySetting.walking = value
        if key == 'chest_pain':
            surveySetting.chest_pain = value
        if key == 'tremor':
            surveySetting.tremor = value
        if key == 'swallowing':
            surveySetting.swallowing = value
        if key == 'pain':
            surveySetting.pain = value
        if key == 'anxiety':
            surveySetting.anxiety = value
        if key == 'seizures':
            surveySetting.seizures = value
        if key == 'rigidity':
            surveySetting.rigidity = value
        if key == 'motivation':
            surveySetting.motivation = value
        if key == 'sleep':
            surveySetting.sleep = value
        if key == 'muscle_spasm':
            surveySetting.muscle_spasm = value
        if key == 'fatigue':
            surveySetting.fatigue = value
        if key == 'hallucinations':
            surveySetting.hallucinations = value
        if key == 'constipation':
            surveySetting.constipation = value

    surveySetting.save()
    patient.surveySetting = surveySetting
    patient.save()
    print(patient.surveySetting)
    print(patient)
    # Validates the form.
    if not form.is_valid():
        print("form is not valid")
        return render(request, 'doctor/set_questionnaire.html', context)

    print(patient.surveySetting)
    print(patient.surveySetting.constipation)
    context['alert_flag'] = True
    return render(request, 'doctor/set_questionnaire.html', context)

def getevents(request):
    doctor = request.user.doctorprofile
    all_events = DoctorCalendarEvent.objects.filter(doctor=doctor)
    event_arr = []
    for i in all_events:
        event_sub_arr = {}
        event_sub_arr['title'] = i.description
        date = i.date.strftime("%Y-%m-%dT")
        start_time = i.start.strftime("%H:%M:%S")
        end_time = i.end.strftime("%H:%M:%S")
        event_sub_arr['start'] = date + start_time
        event_sub_arr['end'] = date + end_time
        event_arr.append(event_sub_arr)
    return HttpResponse(json.dumps(event_arr))

@login_required
@csrf_exempt
def metric_display(request):
    db = get_db()
    patient_user = User.objects.filter(username=request.POST['username'])
    patient = patient_user[0].patientprofile
    patient_id = user_dict[patient.user.id]
    before_n_days = []
    for i in range(1, 30 + 1)[::-1]:
        before_n_days.append(
            str(datetime.date.today() - datetime.timedelta(days=i)))

    diction = {}
    # 1. mood
    retrieved_emotion = find_emotion_by_patient_id(db, patient_id)
    print("fetch emotion")

    # truncate emotion length to 30 days
    if len(retrieved_emotion) > 30:
        retrieved_emotion = retrieved_emotion[len(
            retrieved_emotion) - 30: len(retrieved_emotion)]

    # init mood dict
    diction["mood"] = {"time": before_n_days, "yvalue": {}}
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

    # Biometric:
    # Issue: a) currenlty no tremor data
    #        b) blood pressure is not systolic + diastolic: only one value
    retrieved_biometric = find_biometric_by_patient_id(db, patient_id)
    
    if len(retrieved_biometric) > 30:
        retrieved_biometric = retrieved_biometric[len(
            retrieved_biometric) - 30: len(retrieved_biometric)]

    # 3. blood
    diction["blood"] = {"time": before_n_days, "yvalue": {}}
    diction["blood"]["yvalue"] = {"systolic": [0] * 30, "diastolic": [0] * 30}

    # 4. heartrate
    diction["heartrate"] = {"time": before_n_days, "yvalue": [0] * 30}

    # 5. tremor1
    diction["tremor1"] = {"time": before_n_days, "yvalue": [0] * 30}

    # 6. tremor2
    diction["tremor2"] = {"time": before_n_days, "yvalue": [0] * 30}

    index = 0
    # fill in the dictionary
    for row in retrieved_biometric:
        while (index < 30 - len(retrieved_biometric)):
            index = index + 1

        print(index)
        time = row["created_at"].strftime("%Y-%m-%d")
        systolic = str(row["sbp"])
        diastolic = str(row["dbp"])

        heartrate_value = str(row["heart_rate"])
        # tremor1_value = row["tremor1"]
        # tremor2_value = row["tremor2"]

        diction["blood"]["yvalue"]["systolic"][index] = systolic
        diction["blood"]["yvalue"]["diastolic"][index] = diastolic
        diction["heartrate"]["yvalue"][index] = heartrate_value
        # diction["tremor1"]["yvalue"][index] = tremor1_value
        # diction["tremor2"]["yvalue"][index] = tremor2_value
        index = index + 1

    # print(diction["blood"])
    # print("==================================================================")

    # print(diction["heartrate"])
    # print("==================================================================")

    return HttpResponse(json.dumps(diction), content_type='application/json')
    
@login_required
@csrf_exempt
def game_metric(request):
    db = get_db()
    diction = {}
    patient_user = User.objects.filter(username=request.POST['username'])
    patient = patient_user[0].patientprofile
    patient_id = user_dict[patient.user.id]
    print(patient_id)
    # 2. game
    # Issue: a) Only one game for now

    # truncate emotion length to 30 days
    before_n_days = []
    for i in range(1, 30 + 1)[::-1]:
        before_n_days.append(
            str(datetime.date.today() - datetime.timedelta(days=i)))

    retrieved_game = find_game_by_patient_id(db, patient_id)

    # init game dict
    diction["game"] = {"time": before_n_days, "yvalue": {}}
    diction["game"]["yvalue"] = {"TwistFitEasy": {},
                                 "BeatboxEasy": {}, "WordSearch": [0] * 30,
                                 "TileMatching": [0] * 30, "BrownPeterson": [0] * 30}
    diction["game"]["yvalue"]["TwistFitEasy"] = {
        "left": [0] * 30, "right": [0] * 30}
    diction["game"]["yvalue"]["BeatboxEasy"] = {
        "left": [0] * 30, "right": [0] * 30}

    index1 = 0
    index2 = 0
    index3 = 0
    index4 = 0
    index5 = 0

    # fill in the dictionary
    for row in retrieved_game:
        print(row["game_id"])
        game_id = row["game_id"].hex
        game_name = game_dict[game_id]
        print(game_name)
        if game_name is 'TwistFit_Easy' and index1 < 30:
            left = row["left_hand_score"]
            right = row["right_hand_score"]
            diction["game"]["yvalue"]["TwistFitEasy"]["left"][index1] = left
            diction["game"]["yvalue"]["TwistFitEasy"]["right"][index1] = right
            index1 = index1 + 1
        elif game_name is 'Beatbox_Easy' and index2 < 30:
            left = row["left_hand_score"]
            right = row["right_hand_score"]
            diction["game"]["yvalue"]["BeatboxEasy"]["left"][index2] = left
            diction["game"]["yvalue"]["BeatboxEasy"]["right"][index2] = right
            index2 = index2 + 1
        elif game_name is 'WordSearch' and index3 < 30:
            left = row["left_hand_score"]
            diction["game"]["yvalue"]["WordSearch"][index3] = left
            index3 = index3 + 1
        elif game_name is 'TileMatching' and index4 < 30:
            left = row["left_hand_score"]
            diction["game"]["yvalue"]["TileMatching"][index4] = left
            index4 = index4 + 1
        elif game_name is 'BrownPeterson' and index5 < 30:
            left = row["left_hand_score"]
            diction["game"]["yvalue"]["BrownPeterson"][index5] = left
            index5 = index5 + 1

    diction["game"]["yvalue"]["TwistFitEasy"]["left"].reverse()
    diction["game"]["yvalue"]["TwistFitEasy"]["right"].reverse()
    diction["game"]["yvalue"]["BeatboxEasy"]["left"].reverse()
    diction["game"]["yvalue"]["BeatboxEasy"]["right"].reverse()
    diction["game"]["yvalue"]["WordSearch"].reverse()
    diction["game"]["yvalue"]["TileMatching"].reverse()
    diction["game"]["yvalue"]["BrownPeterson"].reverse()
    print(diction["game"])
    print("==================================================================")

    return HttpResponse(json.dumps(diction), content_type='application/json')


@login_required
@csrf_exempt
def view_general(request):
    db = get_db()
    patient_user = User.objects.filter(username=request.POST['username'])
    patient = patient_user[0].patientprofile
    patient_id = user_dict[patient.user.id]
    print(patient_id)

    diction = {}
    # 1. mood
    retrieved_biometric = find_biometric_by_patient_id(db, patient_id)
    diction["biometric"] = {"time": str(datetime.date.today()), "yvalue": []}

    if len(retrieved_biometric) >= 1:
        heart_rate = str(retrieved_biometric[-1]["heart_rate"])
        diastolic = str(retrieved_biometric[-1]["dbp"])
        systolic = str(retrieved_biometric[-1]["sbp"])
        tremor1 = str(retrieved_biometric[-1]["tremor1"])
        tremor2 = str(retrieved_biometric[-1]["tremor2"])
        diction["biometric"]["yvalue"].append(heart_rate)
        diction["biometric"]["yvalue"].append(diastolic)
        diction["biometric"]["yvalue"].append(systolic)
        diction["biometric"]["yvalue"].append(tremor1)
        diction["biometric"]["yvalue"].append(tremor2)

    return HttpResponse(json.dumps(diction), content_type='application/json')
