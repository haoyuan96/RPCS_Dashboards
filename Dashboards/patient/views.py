from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.forms import model_to_dict
from django.http import HttpResponse
from django.urls import reverse


# Create your views here.

def home(request):
    return render(request, 'patient/index.html')


def todo(request):
    return render(request, 'patient/todo.html')


def calendar(request):
    return render(request, 'patient/calendar.html')


def metrics(request):
    return render(request, 'patient/metrics.html')


def exercises(request):
    return render(request, 'patient/exercises.html')


def survey(request):
    return render(request, 'patient/survey.html')


def login(request):
	context = {}

	# Display the login page if request is "GET"
	if request.method == 'GET':
		return render(request, 'patient/login.html', context)

	# Post request
	if 'email' in request.POST and request.POST['email'] and 'password' in request.POST and request.POST['password']:
		user = authenticate(username=request.POST['username'], password=request.POST['password'])
		if user is not None :
			login(request, user)
			return redirect(reverse('home'))
		# Error case: username doesn't match with password
		else:
			context['error_msg'] = "The email or password is incorrect."

	# Error case:
	else:
		context['error_msg'] = "Please input username and password for login."
	return render(request, 'patient/login.html', context)