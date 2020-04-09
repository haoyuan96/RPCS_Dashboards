from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.forms import model_to_dict
from django.http import HttpResponse
from django.urls import reverse

from .models import CaregiverProfile


# Create your views here.

def home(request):
    profile = request.user.caregiverprofile
    patient = profile.patient.user
    context = {
        'patient': patient
    }
    return render(request, 'caregiver/index.html', context)


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
