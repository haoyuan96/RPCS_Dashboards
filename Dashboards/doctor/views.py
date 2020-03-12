from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.forms import model_to_dict
from django.http import HttpResponse
from django.urls import reverse


# Create your views here.

def home(request):
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