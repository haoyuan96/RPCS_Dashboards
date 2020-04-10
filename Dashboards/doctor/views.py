from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.forms import model_to_dict
from django.http import HttpResponse, Http404
from django.urls import reverse
from django.contrib.auth.models import User
from django.core import serializers


from patient.models import PatientProfile
from doctor.models import DoctorProfile

def home(request):
    context = {}
    doctor = request.user.doctorprofile
    patients = PatientProfile.objects.filter(doctor=doctor)
    context['patients'] = patients
    # patients: list of patient_profile object
    # Usage:
    # name: patient.user.first_name, patient.user.last_name
    # profile_picture: patient.picture
    return render(request, 'doctor/index.html', context)


def search(request):
    if request.method != 'POST':
        raise Http404

    if not 'search_username' in request.POST or not request.POST['search_username']:
        message = 'You must enter the username of a patient.'
        json_error = '{ "error": "'+message+'" }'
        return HttpResponse(json_error, content_type='application/json')

    patient_user = User.object.filter(
        username=request.POST['search_username'])
    if len(patient_user) != 1:
        message = 'Could not find patient with username \'' + \
            request.POST['search_username'] + '\''
        json_error = '{ "error": "'+message+'" }'
        return HttpResponse(json_error, content_type='application/json')

    patient = patient_user[0].patientprofile

    response_text = serializers.serialize('json', patient)
    return HttpResponse(response_text, content_type='application/json')


def add_patient(request):
    context = {}
    if request.method != 'POST':
        print ("404")
        raise Http404
    if not 'search_username' in request.POST or not request.POST['search_username']:
        message = 'You must enter the username of a patient.'
        json_error = '{ "error": "'+message+'" }'
        return HttpResponse(json_error, content_type='application/json')
    
    input_username = request.POST['search_username']
    print(input_username)
    patient_user = User.objects.filter(username=input_username)
    patient = patient_user[0].patientprofile
    doctor = request.user.doctorprofile
    patient.doctor = doctor
    patient.save()

    context['patients'] = doctor.patients.all()
    print(doctor.patients.all())
    return render(request, 'doctor/index.html', context)

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


def view_details(request, username):
    context = {}
    patient_user = User.objects.filter(username=username)
    context['patient'] = patient_user[0].patientprofile
    return render(request, 'doctor/view_details.html', context)


def patient_info(request, username):
    context = {}
    patient_user = User.objects.filter(username=username)
    context['patient']= patient_user[0].patientprofile
    return render(request, 'doctor/patient_info.html', context)


def questionnaire(request, username):
    context = {}
    patient_user = User.objects.filter(username=username)
    context['patient'] = patient_user[0].patientprofile
    return render(request, 'doctor/questionnaire.html', context)


def profile(request):
    return render(request, 'doctor/profile.html')


def set_questionnaire(request, username):
    context = {}
    patient_user = User.objects.filter(username=username)
    context['patient'] = patient_user[0].patientprofile
    return render(request, 'doctor/set_questionnaire.html', context)
