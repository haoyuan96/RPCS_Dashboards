from django.db import models
from django.contrib.auth.models import User
from doctor.models import DoctorProfile
from caregiver.models import CaregiverProfile
import datetime 

# Create your models here.


class PatientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.FileField(blank=True)
    content_type = models.CharField(max_length=50, blank=True)

    caregiver = models.OneToOneField(
        CaregiverProfile, on_delete=models.PROTECT, related_name='patient', null=True)
    doctor = models.ForeignKey(
        DoctorProfile, on_delete=models.PROTECT, related_name='patients', null=True)



class CalendarEvent(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE, related_name='calendar_events')
    start = models.TimeField(auto_now_add=False, null=False)
    end = models.TimeField(auto_now_add=False, null=False)
    descriprion = models.CharField(max_length=200, blank=True)
    date = models.DateField(auto_now_add=False, null=False)

    def __str__(self):
        return 'patient=' + self.patient.user.username + ', start=' + self.start.ToSting() + ', end=' + self.end.ToSting() + ', description=' + self.descriprion
