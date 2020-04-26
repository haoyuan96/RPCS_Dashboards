from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.forms import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import *
from .models import *
from patient.models import *

# create JSON objects (used for calendar events)
from django.core import serializers
import json

from .models import CaregiverProfile
from patient.models import CalendarEvent

from caregiver.forms import *
from patient.forms import *
from .forms import *

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

# Create your views here.
user_dict = {}
user_dict[1] = '0c9ccfdc-833b-11ea-bc55-0242ac130003'
user_dict[2] = '0c9cd270-833b-11ea-bc55-0242ac130003'
user_dict[3] = '0c9cd50e-833b-11ea-bc55-0242ac130003'
user_dict[4] = '0c9cd608-833b-11ea-bc55-0242ac130003'

game_dict = {}
game_dict['d478236c-a361-4ba5-8a70-01a1288c1bb4'] = 'Beatbox_Easy'
game_dict['da62200a-3445-44e0-831d-8a2e20178bb8'] = 'Beatbox_Medium'
game_dict['155c3086-583c-46ad-afcc-782a66255e73'] = 'Beatbox_Hard'
game_dict['e9d2684a-f30c-4002-82fc-a40fde00d8f3'] = 'TwistFit_Easy'
game_dict['6a9df26a-8f51-457c-9972-cbe9b0828a86'] = 'Twistfit_Medium'

def home(request):
    profile = request.user.caregiverprofile
    patient = profile.patient
    print(profile.user.username)
    context = {}
    context['heartrate'] = "90"
    context['blood'] = '123/23'
    context['tremor1'] = '2'
    context['tremor2'] = '3'
    context['patient'] = patient
    return render(request, 'caregiver/index.html', context)
    
def todo(request):
    print(request.user)
    if request.method == 'POST':
        form = TodoEventForm(request.POST)
        if form.is_valid():
            description = form.cleaned_data['description']
            date = form.cleaned_data['date']
            start = form.cleaned_data['start_time']
            end = form.cleaned_data['end_time']
            patient = request.user.caregiverprofile.patient
            print("patient name is: " + patient.user.username)
            newevent = CalendarEvent(patient=patient, description=description, date=date, start=start, end=end)
            newevent.save()
            return redirect("/caregiver/todo")
    form = TodoEventForm()
    context = {'form': form}
    return render(request, 'caregiver/todo.html', context)

def calendar(request):
    if request.method == 'POST':
        form = CalendarEventForm(request.POST)
        if form.is_valid():
            description = form.cleaned_data['description']
            date = form.cleaned_data['date']
            start = form.cleaned_data['start_time']
            end = form.cleaned_data['end_time']
            patient = request.user.caregiverprofile.patient
            print("patient name is: " + patient.user.username)
            newevent = CalendarEvent(patient=patient, description=description, date=date, start=start, end=end)
            newevent.save()
            return redirect("/caregiver/calendar")
    form = CalendarEventForm()
    context = {'form': form}
    return render(request, 'caregiver/calendar.html', context)


def metrics(request):
    return render(request, 'caregiver/metrics.html')

def games(request):
    return render(request, 'caregiver/game_record.html')

def exercises(request):
    return render(request, 'caregiver/exercises.html')


def survey(request):
    context = {}

    caregiver = CaregiverProfile.objects.get(user=request.user)
    patient = caregiver.patient
    print(caregiver.patient)
    # Just display the registration form if this is a GET request.
    if request.method == 'GET':
        form = SurveyForm()
        print("============================================================")
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

        print("============================================================")
        print(form.fields['falls'].widget)
        context['form'] = form
        return render(request, 'caregiver/survey.html', context)

    form = SurveyForm(request.POST)
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

    print(form.fields['falls'].widget)
    context['form'] = form

    if not request.user.is_authenticated:
        print("user is not authenticated")
        return render(request, 'caregiver/survey.html', context)

    
    if caregiver.patient.survey is None:
        survey = Survey()
        survey.save()
        patient.survey = survey
        patient.save()
        caregiver.save()
        print("save new survey")

    print(caregiver.patient.survey)
    for key in request.POST:
        if key == "csrfmiddlewaretoken":
            continue
        value = request.POST[key]

        if key == 'falls':
            caregiver.patient.survey.falls = value
        if key == 'depression':
            caregiver.patient.survey.depression = value
        if key == 'dyskinesia':
            caregiver.patient.survey.dyskinesia = value
        if key == 'movement':
            caregiver.patient.survey.movement = value
        if key == 'thinking':
            caregiver.patient.survey.thinking = value
        if key == 'walking':
            caregiver.patient.survey.walking = value
        if key == 'chest_pain':
            caregiver.patient.survey.chest_pain = value
        if key == 'tremor':
            caregiver.patient.survey.tremor = value
        if key == 'swallowing':
            caregiver.patient.survey.swallowing = value
        if key == 'pain':
            caregiver.patient.survey.pain = value
        if key == 'anxiety':
            caregiver.patient.survey.anxiety = value
        if key == 'seizures':
            caregiver.patient.survey.seizures = value
        if key == 'rigidity':
            caregiver.patient.survey.rigidity = value
        if key == 'motivation':
            caregiver.patient.survey.motivation = value
        if key == 'sleep':
            caregiver.patient.survey.sleep = value
        if key == 'muscle_spasm':
            caregiver.patient.survey.muscle_spasm = value
        if key == 'fatigue':
            caregiver.patient.survey.fatigue = value
        if key == 'hallucinations':
            caregiver.patient.survey.hallucinations = value
        if key == 'constipation':
            caregiver.patient.survey.constipation = value

        caregiver.patient.survey.save()
    caregiver.patient.survey.save()
    print(caregiver.patient.survey)

    context['newuser'] = caregiver
    
    # Validates the form.
    # if not form.is_valid():
    #     print("form is not valid")
    #     return render(request, 'caregiver/survey.html', context)
    # context['alert_flag'] = True
    print(caregiver.patient.survey)
    return render(request, 'caregiver/survey.html', {'form': form, 'alert_flag': True, 'newuser': caregiver})

def login(request):
    return render(request, 'caregiver/login.html')


def register(request):
    return render(request, 'caregiver/register.html')
    
def getevents(request):
    patient = request.user.caregiverprofile.patient
    all_events = CalendarEvent.objects.filter(patient=patient)
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
def metric_display(request):
    db = get_db()
    # patient_id = '10000000-0000-0000-0000-000000000000'
    context = {}

    caregiver = CaregiverProfile.objects.get(user=request.user)
    patient = caregiver.patient
    print(patient.user.id)
    print(user_dict[patient.user.id])
    patient_id = user_dict[patient.user.id]

    diction = {}
    # 1. mood
    retrieved_emotion = find_emotion_by_patient_id(db, patient_id)
    print("fetch emotion")

    # truncate emotion length to 30 days
    if len(retrieved_emotion) > 30:
        retrieved_emotion = retrieved_emotion[len(
            retrieved_emotion) - 30: len(retrieved_emotion)]
    
    before_n_days = []
    for i in range(1, 30 + 1)[::-1]:
        before_n_days.append(str(datetime.date.today() - datetime.timedelta(days=i)))


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
        neutral = str(row["neutral"])
        happiness = str(row["happiness"])
        sadness = str(row["sadness"])
        surprise = str(row["surprise"])
        anger = str(row["anger"])

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
    diction["game"]["time"] = {"game1_time": before_n_days,
                               "game2_time": before_n_days, "game3_time": before_n_days}
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

        # diction["game"]["time"]["game1_time"][index] = time
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
def view_general(request):
    db = get_db()
    patient_id = '10000000-0000-0000-0000-000000000000'
    
    caregiver = CaregiverProfile.objects.get(user=request.user)
    patient = caregiver.patient
    print(patient.user.id)
    print(user_dict[patient.user.id])
    # patient_id = user_dict[patient.user.id]

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
