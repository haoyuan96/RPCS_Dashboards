from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.forms import model_to_dict
from django.http import HttpResponse
from django.urls import reverse
from caregiver.forms import *


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
    context = {}
    # Just display the registration form if this is a GET request.
    if request.method == 'GET':
        context['form'] = SurveyForm()
        return render(request, 'caregiver/survey.html', context)

    # Creates a bound form from the request POST parameters and makes the
    # form available in the request context dictionary.
    form = SurveyForm(request.POST)
    context['form'] = form

    # Validates the form.
    if not form.is_valid():
        print(form)
        return render(request, 'account/survey.html', context)

    # # At this point, the form data is valid.  Register and login the user.
    # new_user = User.objects.create_user(username=form.cleaned_data['username'],
    #                                     password=form.cleaned_data['password1'],
    #                                     email=form.cleaned_data['email'],
    #                                     first_name=form.cleaned_data['first_name'],
    #                                     last_name=form.cleaned_data['last_name'])

    # if 'user_type' not in request.POST:
    #     return render(request, 'account/register.html', context)

    # new_user.save()

    # if request.POST['user_type'] == 'patient':
    #     new_profile = PatientProfile(user=new_user)
    # elif request.POST['user_type'] == 'caregiver':
    #     new_profile = CaregiverProfile(user=new_user)
    # elif request.POST['user_type'] == 'doctor':
    #     new_profile = DoctorProfile(user=new_user)
    # else:
    #     return render(request, 'account/register.html', context)
    # # TODO: caregiver/doctor to connect with patient via username
    # new_profile.save()

    # new_user = authenticate(username=form.cleaned_data['username'],
    #                         password=form.cleaned_data['password1'])

    # login(request, new_user)
    # # TODO: redirect to home for different user
    return render(request, 'caregiver/survey.html')

def login(request):
    return render(request, 'caregiver/login.html')

def register(request):
    return render(request, 'caregiver/register.html')
