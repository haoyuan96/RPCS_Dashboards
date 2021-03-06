from django.urls import path

from . import views

app_name = 'doctor'

urlpatterns = [
    path('', views.home, name='home'),
    path('todo/', views.todo, name='todo'),
    path('calendar/', views.calendar, name='calendar'),
    path('metrics/', views.metrics, name='metrics'),
    path('exercises/', views.exercises, name='exercises'),
    path('survey/', views.survey, name='survey'),
    path('login/', views.login, name='login'),
    path('view_details/<username>', views.view_details, name='view_details'),
    path('game_record/<username>', views.games, name='games'),
    path('questionnaire/<username>', views.questionnaire, name='questionnaire'),
    path('set_questionnaire/<username>',
         views.set_questionnaire, name='set_questionnaire'),
    path('patient_info/<username>', views.patient_info, name='patient_info'),
    path('getevents/', views.getevents, name='getevents'),
    path('register', views.register, name='register'),
    path('profile', views.profile, name='profile'),
    path('add_patient', views.add_patient, name='add_patient'),
    path('search', views.search, name='search'),
    path('metric_display', views.metric_display, name='metric_display'),
    path('game_metric', views.game_metric, name='game_metric')
]
