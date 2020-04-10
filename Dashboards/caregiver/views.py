from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.forms import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import CaregiverProfile
from patient.models import CalendarEvent

from caregiver.forms import *
from patient.forms import *
from .forms import CalendarEventForm

# Create your views here.

def home(request):
    profile = request.user.caregiverprofile
    patient = profile.patient.user
    context = {
        'patient': patient
    }
    return render(request, 'caregiver/index.html', context)


def todo(request):
    print(request.user)
    return render(request, 'caregiver/todo.html')


def calendar(request):
    form = CalendarEventForm()
    context = {'form': form}
    return render(request, 'caregiver/calendar.html', context)


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
    
def addevent(request):
    if request.method == 'POST':
        form = CalendarEventForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data['description'])
            # print(form.cleaned_data['date'])
            # print(form.cleaned_data['start_time'])
            # print(form.cleaned_data['end_time'])
            description = form.cleaned_data['description']
            date = form.cleaned_data['date']
            start = form.cleaned_data['start_time']
            end = form.cleaned_data['end_time']
            patient = request.user.caregiverprofile.patient
            print("patient name is: " + patient.user.username)
            newevent = CalendarEvent(patient=patient, descriprion=description, date=date, start=start, end=end)
            newevent.save()
            return render(request, 'caregiver/todo.html')
    return render(request, 'caregiver/survey.html')
