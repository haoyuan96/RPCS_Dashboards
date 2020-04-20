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
from doctor.forms import DoctorCalendarEventForm
from caregiver.forms import CalendarEventForm
from patient.models import PatientProfile, Survey, CalendarEvent, SurveySetting
from doctor.models import DoctorProfile, DoctorCalendarEvent
from django.contrib import messages
from .forms import SurveySettingForm
from django import forms
# create JSON objects (used for calendar events)
from django.core import serializers
import json


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
    if request.method == 'POST':
        form = DoctorCalendarEventForm(request.POST)
        if form.is_valid():
            description = form.cleaned_data['description']
            date = form.cleaned_data['date']
            start = form.cleaned_data['start_time']
            end = form.cleaned_data['end_time']
            patient_id = form.cleaned_data['patient']

            # add to doctor
            doctor = request.user.doctorprofile
            newevent = DoctorCalendarEvent(doctor=doctor, description=description, date=date, start=start, end=end)
            newevent.save()

            # add to patient
            patient = User.objects.get(username=patient_id)
            if (patient):
                patient = patient.patientprofile
                print("patient name is: " + patient.user.username)
                newevent = CalendarEvent(patient=patient, description=description, date=date, start=start, end=end)
                newevent.save()
            return redirect("/doctor/calendar")

    form = DoctorCalendarEventForm()
    context = {'form': form}
    return render(request, 'doctor/calendar.html', context)


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
    print("here")
    context = {}
    patient_user = User.objects.filter(username=username)
    patient = patient_user[0].patientprofile
    context['patient'] = patient
    survey = patient.survey
    surveySetting = patient.surveySetting
    if survey is None:
        context['exist_alert'] = 0
    else:
        
        fields = []
        for key, value in survey.__dict__.items():
            print(key, '  =>  ', value)
            if surveySetting.__dict__[key] is True and value == 5:
                fields.append(key)
        context['alert_fields'] = fields
        if len(fields) >= 4:
            context['exist_alert'] = 2
            context['alert_fields'] = fields[0:3]
            context['count'] = len(fields) - 3
        elif len(fields) == 0:
            context['exist_alert'] = 0
        else:
            context['exist_alert'] = 1
            context['count'] = len(fields)
        print(fields)
    return render(request, 'doctor/patient_info.html', context)


def questionnaire(request, username):
    context = {}
    patient_user = User.objects.filter(username=username)
    patient = patient_user[0].patientprofile
    context['patient'] = patient
    if patient_user[0].patientprofile.survey is None:
        form = SurveyForm()
    else:
        form = SurveyForm(data=model_to_dict(
            Survey.objects.get(pk=patient_user[0].patientprofile.survey.id)))
    
    
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
    
    context['form'] = form

    return render(request, 'doctor/questionnaire.html', {'form': form, 'patient': patient_user[0].patientprofile})

    # return render(request, 'doctor/questionnaire.html', context)


def profile(request):
    return render(request, 'doctor/profile.html')

def set_questionnaire(request, username):
    context = {}
    patient_user = User.objects.filter(username=username)
    context['patient'] = patient_user[0].patientprofile
    if request.method == 'GET':
        if patient_user[0].patientprofile.surveySetting is None:
            object = SurveySettingForm()
        else:
            object = SurveySettingForm(data=model_to_dict(
                SurveySetting.objects.get(pk=patient_user[0].patientprofile.surveySetting.id)))
        context['form'] = object
        return render(request, 'doctor/set_questionnaire.html', context)

    # # if patient_user[0].patientprofile.surveySetting is None:
    # #     object = SurveySettingForm()
    # # else:
    # #     object = SurveySettingForm(data=model_to_dict(
    # #         SurveySetting.objects.get(pk=patient_user[0].patientprofile.surveySetting.id)))
    # # context['form'] = object


    # # Just display the registration form if this is a GET request.
    # if request.method == 'GET':
    #     context['form'] = SurveySettingForm()
    #     return render(request, 'doctor/set_questionnaire.html', context)

    form = SurveySettingForm(request.POST)
    context['form'] = form

    if not request.user.is_authenticated:
        print("user is not authenticated")
        return render(request, 'doctor/set_questionnaire.html', context)

    patient_user = User.objects.filter(username=username)
    patient = patient_user[0].patientprofile
    
    print(patient.surveySetting)
    surveySetting = patient.surveySetting
    for key in request.POST:
        if key == "csrfmiddlewaretoken":
            continue
        value = request.POST[key]

        if key == 'falls':
            surveySetting.falls = value
        if key == 'depression':
            surveySetting.depression = value
        if key == 'dyskinesia':
            surveySetting.dyskinesia = value
        if key == 'movement':
            surveySetting.movement = value
        if key == 'thinking':
            surveySetting.thinking = value
        if key == 'walking':
            surveySetting.walking = value
        if key == 'chest_pain':
            surveySetting.chest_pain = value
        if key == 'tremor':
            surveySetting.tremor = value
        if key == 'swallowing':
            surveySetting.swallowing = value
        if key == 'pain':
            surveySetting.pain = value
        if key == 'anxiety':
            surveySetting.anxiety = value
        if key == 'seizures':
            surveySetting.seizures = value
        if key == 'rigidity':
            surveySetting.rigidity = value
        if key == 'motivation':
            surveySetting.motivation = value
        if key == 'sleep':
            surveySetting.sleep = value
        if key == 'muscle_spasm':
            surveySetting.muscle_spasm = value
        if key == 'fatigue':
            surveySetting.fatigue = value
        if key == 'hallucinations':
            surveySetting.hallucinations = value
        if key == 'constipation':
            surveySetting.constipation = value

    surveySetting.save()
    patient.surveySetting = surveySetting
    patient.save()
    print(patient.surveySetting)
    print(patient)
    # Validates the form.
    if not form.is_valid():
        print("form is not valid")
        return render(request, 'doctor/set_questionnaire.html', context)

    print(patient.surveySetting)
    print(patient.surveySetting.constipation)
    context['alert_flag'] = True
    return render(request, 'doctor/set_questionnaire.html', context)

def getevents(request):
    doctor = request.user.doctorprofile
    all_events = DoctorCalendarEvent.objects.filter(doctor=doctor)
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
