from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.forms import model_to_dict
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User

from .forms import RegistrationForm, LoginForm
from patient.models import PatientProfile
from caregiver.models import CaregiverProfile
from doctor.models import DoctorProfile

from patient.views import home as patient_home
from caregiver.views import home as caregiver_home
from doctor.views import home as doctor_home

home_views = {
    "patient": patient_home,
    "caregiver": caregiver_home,
    "doctor": doctor_home,
}
# Create your views here.


def homepage(request):
    # TODO: do we need a homepage? Or just show the login/register page?
    return render(request, 'homepage.html')


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

    if request.POST['user_type'] == 'patient':
        new_profile = PatientProfile(user=new_user)
    elif request.POST['user_type'] == 'caregiver':
        new_profile = CaregiverProfile(user=new_user)
    elif request.POST['user_type'] == 'doctor':
        new_profile = DoctorProfile(user=new_user)
    else:
        return render(request, 'account/register.html', context)
    new_profile.save()
    # TODO: caregiver to connect with patient via username

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
    return redirect(reverse('homepage'))


def logout_action(request):
    logout(request)
    return redirect(reverse('login'))
