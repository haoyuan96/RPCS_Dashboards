from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.forms import model_to_dict
from django.http import HttpResponse
from django.urls import reverse


# Create your views here.

def home(request):
    return render(request, 'doctor/index.html')


def todo(request):
    return render(request, 'doctor/todo.html')


def calendar(request):
    return render(request, 'doctor/calendar.html')


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


def view_details(request):
    return render(request, 'doctor/view_details.html')


def patient_info(request):
    return render(request, 'doctor/patient_info.html')


def questionnaire(request):
	return render(request, 'doctor/questionnaire.html')


def profile(request):
    return render(request, 'doctor/profile.html')
    

