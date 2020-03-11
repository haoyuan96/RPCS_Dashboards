from django.urls import path

from . import views

app_name = 'caregiver'

urlpatterns = [
    path('', views.home, name='home'),
    path('todo', views.todo, name='todo'),
    path('calendar', views.calendar, name='calendar'),
    path('metrics', views.metrics, name='metrics'),
    path('exercises', views.exercises, name='exercises'),
    path('survey', views.survey, name='survey'),
    path('login', views.login, name='login'),
]