from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.forms import model_to_dict
from django.http import HttpResponse
from django.urls import reverse
from patient.forms import *
from .models import Survey, PatientProfile

#-----------------------
# For the Database
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
    db = get_db()

    accel_id = uuid.uuid4()
    description = "patient dashboard local test"
    patient_id = uuid.uuid4()
    x = 2.3
    y = 2.3
    z = 2.3
    # db, accel_id, description, patient_id, x, y, z
    insert_accel(db, accel_id, description, patient_id, x, y, z)

    # verify data
    retrieved_accel = []
    print("accel_id to find: ", accel_id)
    retrieved_accel = find_by_accel_id(db, accel_id)
    print(retrieved_accel)
    return render(request, 'patient/index.html')


def todo(request):
    return render(request, 'patient/todo.html')


def calendar(request):
    return render(request, 'patient/calendar.html')


def metrics(request):
    return render(request, 'patient/metrics.html')


def exercises(request):
    return render(request, 'patient/exercises.html')


def survey(request):
    context = {}
    
    # Just display the registration form if this is a GET request.
    if request.method == 'GET':
        context['form'] = SurveyForm()
        return render(request, 'patient/survey.html', context)


    form = SurveyForm(request.POST)
    context['form'] = form  
    
    if not request.user.is_authenticated:
        print("user is not authenticated")
        return render(request, 'patient/survey.html', context)
    
    patient = PatientProfile.objects.get(user=request.user)
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
    if not form.is_valid():
        print("form is not valid")
        return render(request, 'patient/survey.html', context)

    print(patient.survey)
    print(patient.survey.constipation)

    # if patient.survey is None:
    #     patient.survey = Survey()
    #     patient.survey.save()
    #     # patient.save()
    #     print("save new survey")

    # print(patient.survey)
    # for key in request.POST:
    #     if key == "csrfmiddlewaretoken":
    #         continue
    #     value = request.POST[key]
        
    #     if key == 'falls':
    #         patient.survey.falls = value
    #     if key == 'depression':
    #         patient.survey.depression = value
    #     if key == 'dyskinesia':
    #         patient.survey.dyskinesia = value
    #     if key == 'movement':
    #         patient.survey.movement = value
    #     if key == 'thinking':
    #         patient.survey.thinking = value
    #     if key == 'walking':
    #         patient.survey.walking = value
    #     if key == 'chest_pain':
    #         patient.survey.chest_pain = value
    #     if key == 'tremor':
    #         patient.survey.tremor = value
    #     if key == 'swallowing':
    #         patient.survey.swallowing = value
    #     if key == 'pain':
    #         patient.survey.pain = value
    #     if key == 'anxiety':
    #         patient.survey.anxiety = value
    #     if key == 'seizures':
    #         patient.survey.seizures = value
    #     if key == 'rigidity':
    #         patient.survey.rigidity = value
    #     if key == 'motivation':
    #         patient.survey.motivation = value
    #     if key == 'sleep':
    #         patient.survey.sleep = value
    #     if key == 'muscle_spasm':
    #         patient.survey.muscle_spasm = value
    #     if key == 'fatigue':
    #         patient.survey.fatigue = value
    #     if key == 'hallucinations':
    #         patient.survey.hallucinations = value
    #     if key == 'constipation':
    #         patient.survey.constipation = value
       
    #     patient.survey.save()
    # patient.survey.save()
    # print(patient.survey)
    # print(patient)
    # # Validates the form.
    # if not form.is_valid():
    #     print("form is not valid")
    #     return render(request, 'patient/survey.html', context)
    
    # print(patient.survey)
    # print(patient.survey.constipation)

    return render(request, 'patient/survey.html', context)


def login(request):
	context = {}

	# Display the login page if request is "GET"
	if request.method == 'GET':
		return render(request, 'patient/login.html', context)

	# Post request
	if 'email' in request.POST and request.POST['email'] and 'password' in request.POST and request.POST['password']:
		user = authenticate(username=request.POST['username'], password=request.POST['password'])
		if user is not None :
			login(request, user)
			return redirect(reverse('home'))
		# Error case: username doesn't match with password
		else:
			context['error_msg'] = "The email or password is incorrect."

	# Error case:
	else:
		context['error_msg'] = "Please input username and password for login."
	return render(request, 'patient/login.html', context)

