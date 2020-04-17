from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.forms import model_to_dict
from django.http import HttpResponse
from django.urls import reverse

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

def home(request):
    # return HttpResponse(json.dumps(diction), content_type='application/json')
    return render(request, 'caregiver/index.html')


def todo(request):
    return render(request, 'caregiver/todo.html')


def calendar(request):
    return render(request, 'caregiver/calendar.html')


def metrics(request):
    return render(request, 'caregiver/metrics.html')


def exercises(request):
    return render(request, 'caregiver/exercises.html')


def survey(request):
    return render(request, 'caregiver/survey.html')


def login(request):
    return render(request, 'caregiver/login.html')

def register(request):
    return render(request, 'caregiver/register.html')


@login_required
def metric_display(request):
    db = get_db()
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
    diction["game"]["time"] = {"game1_time": [
        "0000-00-00"] * 30, "game2_time": ["0000-00-00"] * 30, "game3_time": ["0000-00-00"] * 30}
    diction["game"]["yvalue"] = {"WordSearch": [
        0] * 30, "TileMatching": [0] * 30, "Brown-Peterson": [0] * 30}
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
