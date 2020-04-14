from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.forms import model_to_dict
from django.http import HttpResponse
from django.urls import reverse
from patient.forms import *
from caregiver.forms import TodoEventForm
from .models import Survey, PatientProfile, CalendarEvent


# create JSON objects (used for calendar events)
from django.core import serializers
import json


# Create your views here.

def home(request):
    return render(request, 'patient/index.html')


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
            newevent = CalendarEvent(patient=patient, description=description, date=date, start=start, end=end)
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
    return render(request, 'patient/survey.html', {'form': form, 'alert_flag' : True})


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

