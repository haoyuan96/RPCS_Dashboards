from django.urls import path

from . import views

app_name = 'unoGame'
urlpatterns = [
    path('', views.home, name='home'),
]
