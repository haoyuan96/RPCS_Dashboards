from django.db import models
from django.contrib.auth.models import User
from doctor.models import DoctorProfile
# from patient.models import PatientProfile
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


class CaregiverProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.FileField(blank=True)
    content_type = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return 'id=' + str(self.id)
