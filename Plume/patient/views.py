import sys
from ipdb import set_trace as debug
import colored_traceback.always
import uuid
import json
from io import BytesIO
from database.database import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.forms import model_to_dict
from django.http import HttpResponse
from django.urls import reverse
from patient.forms import *
from caregiver.forms import TodoEventForm
from .models import Survey, PatientProfile, CalendarEvent, SurveySetting
from django import forms


# create JSON objects (used for calendar events)
from django.core import serializers
import json

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

# -----------------------
# For the Database
sys.path.append('database')
# import pycurl
# Create your views here.


def home(request):
    # db = get_db()

    # accel_id = uuid.uuid4()
    # description = "patient dashboard local test"
    # patient_id = uuid.uuid4()
    # x = 2.3
    # y = 2.3
    # z = 2.3
    # # db, accel_id, description, patient_id, x, y, z
    # insert_accel(db, accel_id, description, patient_id, x, y, z)

    # # verify data
    # retrieved_accel = []
    # print("accel_id to find: ", accel_id)
    # retrieved_accel = find_by_accel_id(db, accel_id)
    # print(retrieved_accel)
    context = {}
    score = get_score()
    # TODO: need to decide the thresholds of the performance
    if score > 100:
        context['img_path'] = 'img/emoji_smile.png'
        context['sentence'] = 'You are doing well today! Keep up!'
    elif 50 < score <= 100:
        context['img_path'] = 'img/emoji_soso.png'
        context['sentence'] = 'Good good!'
    else:
        context['img_path'] = 'img/emoji_sad.png'
        context['sentence'] = 'Cheer up!'
    return render(request, 'patient/index.html', context)


def get_score():
    # TODO: get data from db and return computed score of the patient
    return 200


def todo(request):
    print(request.user)
    if request.method == 'POST':
        form = TodoEventForm(request.POST)
        if form.is_valid():
            description = form.cleaned_data['description']
            date = form.cleaned_data['date']
            start = form.cleaned_data['start_time']
            end = form.cleaned_data['end_time']
            patient = request.user.patientprofile
            print("patient name is: " + patient.user.username)
            newevent = CalendarEvent(
                patient=patient, description=description, date=date, start=start, end=end)
            newevent.save()
            return redirect("/patient/todo")
    print(TodoEventForm)
    form = TodoEventForm()
    context = {'form': form}
    return render(request, 'patient/todo.html', context)


def calendar(request):
    return render(request, 'patient/calendar.html')


def getevents(request):
    patient = request.user.patientprofile
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


def metrics(request):
    context = {}
    try:
        db = get_db()
        patient_id = user_dict[request.user.id]
        # get latest biometric data from db
        if len(find_biometric_by_patient_id(db, patient_id)) == 0:
            context['systolic'] = '0'
            context['diastolic'] = '0'
            context['heart_rate'] = '0'
            context['word_search'] = '0'
            context['tile_matching'] = '0'
            return render(request, 'patient/metrics.html', context)

        retrieved_biometric = find_biometric_by_patient_id(db, patient_id)[-1]
        # TODO: need to change here when blood pressure schma is updated
        context['systolic'] = retrieved_biometric['sbp']
        context['diastolic'] = retrieved_biometric['dbp']
        context['heart_rate'] = retrieved_biometric['heart_rate']
        # context['tremor1'] = retrieved_biometric['tremor1']
        # context['tremor2'] = retrieved_biometric['tremor2']

        # game
        game_dict = {}
        game_dict['d478236ca3614ba58a7001a1288c1bb4'] = 'Beatbox_Easy'
        game_dict['da62200a344544e0831d8a2e20178bb8'] = 'Beatbox_Medium'
        game_dict['155c3086583c46adafcc782a66255e73'] = 'Beatbox_Hard'
        game_dict['e9d2684af30c400282fca40fde00d8f3'] = 'TwistFit_Easy'
        game_dict['6a9df26a8f51457c9972cbe9b0828a86'] = 'Twistfit_Medium'
        game_dict['1'] = 'WordSearch'
        game_dict['2'] = 'TileMatching'
        game_dict['3'] = 'BrownPeterson'

        retrieved_game = find_game_by_patient_id(db, patient_id)[::-1]
        for row in retrieved_game:
            game_id = row["game_id"].hex
            game_name = game_dict[game_id]
            score = (row["left_hand_score"] + row["right_hand_score"]) / 2
            # print(game_name)
            if game_name is 'TwistFit_Easy' and 'twistfit' not in context:
                context['twistfit'] = score
            elif game_name is 'Beatbox_Easy' and 'beatbox' not in context:
                context['beatbox'] = score
            elif game_name is 'WordSearch' and 'word_search' not in context:
                context['word_search'] = score
            elif game_name is 'TileMatching' and 'tile_matching' not in context:
                context['tile_matching'] = score
            elif game_name is 'BrownPeterson' and 'brown_peterson' not in context:
                context['brown_peterson'] = score
            if 'twistfit' in context and 'beatbox' in context and 'word_search' in context and 'tile_matching' in context and 'brown_peterson' in context:
                # print(context)
                break
    except Exception as e:
        print(e)
    return render(request, 'patient/metrics.html', context)


def exercises(request):
    return render(request, 'patient/exercises.html')


def survey(request):
    context = {}

    patient = PatientProfile.objects.get(user=request.user)
    print(patient.surveySetting)
    # Just display the registration form if this is a GET request.
    if request.method == 'GET':

        form = SurveyForm()

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
        return render(request, 'patient/survey.html', context)

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
        return render(request, 'patient/survey.html', context)

    if patient.survey is None:
        survey = Survey()
        survey.save()
        patient.survey = survey
        patient.save()
        print("save new survey")

    print(patient.survey)
    survey = patient.survey
    for key in request.POST:
        if key == "csrfmiddlewaretoken":
            continue
        value = request.POST[key]

        if key == 'falls':
            survey.falls = value
        if key == 'depression':
            survey.depression = value
        if key == 'dyskinesia':
            survey.dyskinesia = value
        if key == 'movement':
            survey.movement = value
        if key == 'thinking':
            survey.thinking = value
        if key == 'walking':
            survey.walking = value
        if key == 'chest_pain':
            survey.chest_pain = value
        if key == 'tremor':
            survey.tremor = value
        if key == 'swallowing':
            survey.swallowing = value
        if key == 'pain':
            survey.pain = value
        if key == 'anxiety':
            survey.anxiety = value
        if key == 'seizures':
            survey.seizures = value
        if key == 'rigidity':
            survey.rigidity = value
        if key == 'motivation':
            survey.motivation = value
        if key == 'sleep':
            survey.sleep = value
        if key == 'muscle_spasm':
            survey.muscle_spasm = value
        if key == 'fatigue':
            survey.fatigue = value
        if key == 'hallucinations':
            survey.hallucinations = value
        if key == 'constipation':
            survey.constipation = value

    survey.save()
    patient.survey = survey
    patient.save()
    print(patient.survey)
    print(patient)
    # Validates the form.
    # if not form.is_valid():
    #     print("form is not valid")
    #     return render(request, 'patient/survey.html', context)

    print(patient.survey)
    print(patient.survey.constipation)
    return render(request, 'patient/survey.html', {'form': form, 'alert_flag': True})


def login(request):
    context = {}

    # Display the login page if request is "GET"
    if request.method == 'GET':
        return render(request, 'patient/login.html', context)

    # Post request
    if 'email' in request.POST and request.POST['email'] and 'password' in request.POST and request.POST['password']:
        user = authenticate(
            username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect(reverse('home'))
        # Error case: username doesn't match with password
        else:
            context['error_msg'] = "The email or password is incorrect."

    # Error case:
    else:
        context['error_msg'] = "Please input username and password for login."
    return render(request, 'patient/login.html', context)
