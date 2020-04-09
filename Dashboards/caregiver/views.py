from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.forms import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


from caregiver.forms import *
from patient.forms import *
from .forms import CalendarEventForm

# Create your views here.

def home(request):
    return render(request, 'caregiver/index.html')


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
            print(form.cleaned_data['description'])
            print(form.cleaned_data['date'])
            print(form.cleaned_data['start_time'])
            print(form.cleaned_data['end_time'])
            patient = request.user.patient
            #event = CalendarEvent(patient=patient, phone_number=number, date_subscribed=datetime.now(), messages_received=0)
    return render(request, 'caregiver/todo.html')