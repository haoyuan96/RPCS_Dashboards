from django.urls import path

from . import views

app_name = 'doctor'

urlpatterns = [
    path('', views.home, name='home'),
    path('todo', views.todo, name='todo'),
    path('calendar', views.calendar, name='calendar'),
    path('metrics', views.metrics, name='metrics'),
    path('exercises', views.exercises, name='exercises'),
    path('survey', views.survey, name='survey'),
    path('login', views.login, name='login'),
    path('view_details', views.view_details, name='view_details'),
    path('questionnaire', views.questionnaire, name='questionnaire'),
    path('patient_info', views.patient_info, name='patient_info'),
    

]
