from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.forms import model_to_dict
from django.http import HttpResponse, Http404
from django.urls import reverse
from django.contrib.auth.models import User
from django.core import serializers
# from django.shortcuts import render_to_response
from patient.forms import SurveyForm
from patient.models import PatientProfile, Survey
from doctor.models import DoctorProfile
from django.contrib import messages

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
    context = {}
    print('search now')
    if request.method != 'POST':
        print('Http404')
        raise Http404

    doctor = request.user.doctorprofile
    if not 'search_username' in request.POST or not request.POST['search_username']:
        # message = 'You must enter the username of a patient.'
        # json_error = '{ "error": "'+message+'" }'
        # return HttpResponse(json_error, content_type='application/json')
    
        message = 'You must enter a valid username of a patient.'
        return render(request, 'doctor/index.html', {'search_alert_flag': True, 'patients': doctor.patients.all()})

    
    
    if 'search_username' in request.POST and request.POST['search_username'] != '':
        try:
            user = User.objects.get(username=request.POST['search_username'])
            print('print out!!!!!', user)
            search_patient = PatientProfile.objects.filter(user=user)
            print('print out!!!!!', search_patient)
            if len(search_patient) != 1:
                context['patients'] = doctor.patients.all()
                return render(request, 'doctor/index.html', context)
            else:
                print('search_patient found')
                if search_patient[0].doctor != doctor:
                    print('not correct doctor')
                    print(search_patient[0].doctor)
                    context['patients'] = doctor.patients.all()
                    return render(request, 'doctor/index.html', context)
                print('correct doctor')
                context['patients'] = search_patient
                print('return only one patient')
                return render(request, 'doctor/index.html', context)
        except:
            print('try fail')
            context['patients'] = doctor.patients.all()
            return render(request, 'doctor/index.html', {'search_alert_flag': True, 'patients': doctor.patients.all()})
    else:
        print('no request post')
        context['patients'] = doctor.patients.all()
    return render(request, 'doctor/index.html', context)

def add_patient(request):
    context = {}
    print("100")
    if request.method != 'POST':
        print ("404")
        raise Http404

    doctor = request.user.doctorprofile
    if not 'search_username' in request.POST or not request.POST['search_username']:
        # message = 'You must enter a valid username of a patient.'

        # json_error = '{ "error": "'+message+'" }'
        # return HttpResponse(json_error, content_type='application/json')
        return render(request, 'doctor/index.html', {'alert_flag': True, 'patients': doctor.patients.all()})

    try:
        input_username = request.POST['search_username']
        print(input_username)
        patient_user = User.objects.filter(username=input_username)
        patient = patient_user[0].patientprofile
        
        # ignore already added ones
        if not patient.doctor is doctor :
            patient.doctor = doctor
            patient.save()

        context['patients'] = doctor.patients.all()
        print(doctor.patients.all())
    except:
        print('try fail')
        return render(request, 'doctor/index.html', {'alert_flag': True, 'patients': doctor.patients.all()})

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
    context['form'] = patient_user[0].patientprofile.survey
    # print(patient_user[0])
    # print(patient_user[0].patientprofile)
    # print(patient_user[0].patientprofile.survey)
    print(patient_user[0].patientprofile.survey.constipation)
    object = SurveyForm(data=model_to_dict(
        Survey.objects.get(pk=patient_user[0].patientprofile.survey.id)))
    return render(request, 'doctor/questionnaire.html', {'form': object, 'patient': patient_user[0].patientprofile})

    # return render(request, 'doctor/questionnaire.html', context)


def profile(request):
    return render(request, 'doctor/profile.html')


def set_questionnaire(request, username):
    context = {}
    patient_user = User.objects.filter(username=username)
    context['patient'] = patient_user[0].patientprofile
    return render(request, 'doctor/set_questionnaire.html', context)
