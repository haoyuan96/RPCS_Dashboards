from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.forms import model_to_dict
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User

from patient.forms import RegistrationForm
from patient.models import PatientProfile
from caregiver.models import CaregiverProfile
from doctor.models import DoctorProfile

# Create your views here.


def homepage(request):
    return render(request, 'homepage.html')


def register(request):
    context = {}
    # Just display the registration form if this is a GET request.
    if request.method == 'GET':
        context['form'] = RegistrationForm()
        return render(request, 'register.html', context)

    # Creates a bound form from the request POST parameters and makes the
    # form available in the request context dictionary.
    form = RegistrationForm(request.POST)
    context['form'] = form

    # Validates the form.
    if not form.is_valid():
        print(form)
        return render(request, 'register.html', context)

    # At this point, the form data is valid.  Register and login the user.
    new_user = User.objects.create_user(username=form.cleaned_data['username'],
                                        password=form.cleaned_data['password1'],
                                        email=form.cleaned_data['email'],
                                        first_name=form.cleaned_data['first_name'],
                                        last_name=form.cleaned_data['last_name'])

    if 'user_type' not in request.POST:
        return render(request, 'register.html', context)

    new_user.save()

    if request.POST['user_type'] == 'patient':
        new_profile = PatientProfile(user=new_user)
    elif request.POST['user_type'] == 'caregiver':
        new_profile = CaregiverProfile(user=new_user)
    elif request.POST['user_type'] == 'doctor':
        new_profile = DoctorProfile(user=new_user)
    else:
        return render(request, 'register.html', context)

    new_profile.save()

    new_user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password1'])

    login(request, new_user)
    return redirect(reverse('homepage'))
