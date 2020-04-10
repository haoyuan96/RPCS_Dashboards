from django.db import models
from django.contrib.auth.models import User
from caregiver.models import CaregiverProfile
from doctor.models import DoctorProfile

# Create your models here.


class PatientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.FileField(blank=True)
    content_type = models.CharField(max_length=50, blank=True)

    caregiver = models.OneToOneField(
        CaregiverProfile, on_delete=models.PROTECT, related_name='patient', null=True)
    doctor = models.ForeignKey(
        DoctorProfile, on_delete=models.PROTECT, related_name='patients', null=True)