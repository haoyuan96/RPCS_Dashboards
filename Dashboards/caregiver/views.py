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

# Create your views here.

def home(request):
    profile = request.user.caregiverprofile
    patient = profile.patient
    print(profile.user.username)
    context = {
        'patient': patient
    }
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
