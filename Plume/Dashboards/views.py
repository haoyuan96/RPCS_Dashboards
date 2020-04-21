from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.forms import model_to_dict
from django.http import HttpResponse, request
from django.urls import reverse
from django.contrib.auth.models import User

from .forms import RegistrationForm, LoginForm
from patient.models import PatientProfile, SurveySetting, Survey
from caregiver.models import CaregiverProfile
from doctor.models import DoctorProfile
from doctor.forms import SurveySettingForm

# Create your views here.


# def homepage(request):
#     # TODO: do we need a homepage? Or just show the login/register page?
#     return render(request, 'account/login.html')


def register(request):
    context = {}
    # Just display the registration form if this is a GET request.
    if request.method == 'GET':
        context['form'] = RegistrationForm()
        return render(request, 'account/register.html', context)

    # Creates a bound form from the request POST parameters and makes the
    # form available in the request context dictionary.
    form = RegistrationForm(request.POST)
    context['form'] = form

    # Validates the form.
    if not form.is_valid():
        print(form)
        return render(request, 'account/register.html', context)

    # At this point, the form data is valid.  Register and login the user.
    new_user = User.objects.create_user(username=form.cleaned_data['username'],
                                        password=form.cleaned_data['password1'],
                                        email=form.cleaned_data['email'],
                                        first_name=form.cleaned_data['first_name'],
                                        last_name=form.cleaned_data['last_name'])

    if 'user_type' not in request.POST:
        return render(request, 'account/register.html', context)

    new_user.save()
    new_user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password1'])
    login(request, new_user)

    print(form.cleaned_data['username'])
    if request.POST['user_type'] == 'patient':
        new_profile = PatientProfile(user=new_user)
        # survey = Survey()
        surveySetting = SurveySetting()
        # survey.save()
        surveySetting.save()
        new_profile.surveySetting = surveySetting
        # new_profile.survey = survey
        # new_profile.save()
        
        new_profile.save()
        print("save new survey")
        print(new_profile.id)

    elif request.POST['user_type'] == 'caregiver':
        new_profile = CaregiverProfile(user=new_user)
        new_profile.save()
        if 'patient_username' in request.POST:
            patient_username = request.POST['patient_username']
            patient_user = User.objects.filter(username=patient_username)
            if len(patient_user) > 0:
                patient = patient_user[0].patientprofile
                print(patient)
                patient.caregiver = new_profile
                patient.save()
    elif request.POST['user_type'] == 'doctor':
        new_profile = DoctorProfile(user=new_user)
        new_profile.save()
    else:
        return render(request, 'account/register.html', context)

    # redirect to home for different user
    return redirect(reverse(request.POST['user_type'] + ':home'))


def login_view(request):
    context = {}

    # Just display the registration form if this is a GET request.
    if request.method == 'GET':
        context['form'] = LoginForm()
        return render(request, 'account/login.html', context)

    # Creates a bound form from the request POST parameters and makes the
    # form available in the request context dictionary.
    form = LoginForm(request.POST)
    context['form'] = form
    # Validates the form.
    if not form.is_valid():
        print("invalid")
        print(form.non_field_errors())
        context['error_msg'] = form.non_field_errors()
        return render(request, 'account/login.html', context)

    new_user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'])

    login(request, new_user)
    # TODO: redirect to home for different user
    if hasattr(request.user, 'caregiverprofile'):
        return redirect(reverse('caregiver:home'))
    elif hasattr(request.user, 'doctorprofile'):
        return redirect(reverse('doctor:home'))
    elif hasattr(request.user, 'patientprofile'):
        return redirect(reverse('patient:home'))

    return redirect(reverse('login'))


def logout_action(request):
    logout(request)
    return redirect(reverse('login'))
