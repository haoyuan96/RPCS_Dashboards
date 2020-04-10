from django.db import models
from django.contrib.auth.models import User
from doctor.models import DoctorProfile
from caregiver.models import CaregiverProfile
import datetime 
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Survey(models.Model):
    falls = models.IntegerField(
        blank=True, 
        default=1,
        validators=[MaxValueValidator(5), MinValueValidator(0)]
     )

    depression = models.IntegerField(
        blank=True,
        default=1,
        validators=[MaxValueValidator(5), MinValueValidator(0)]
    )

    dyskinesia = models.IntegerField(
        blank=True,
        default=1,
        validators=[MaxValueValidator(5), MinValueValidator(0)]
    )

    movement = models.IntegerField(
        blank=True,
        default=1,
        validators=[MaxValueValidator(5), MinValueValidator(0)]
    )

    thinking = models.IntegerField(
        blank=True,
        default=1,
        validators=[MaxValueValidator(5), MinValueValidator(0)]
    )
    
    walking = models.IntegerField(
        blank=True,
        default=1,
        validators=[MaxValueValidator(5), MinValueValidator(0)]
    )

    chest_pain = models.IntegerField(
        blank=True,
        default=1,
        validators=[MaxValueValidator(5), MinValueValidator(0)]
    )

    tremor = models.IntegerField(
        blank=True,
        default=1,
        validators=[MaxValueValidator(5), MinValueValidator(0)]
    )

    swallowing = models.IntegerField(
        blank=True,
        default=1,
        validators=[MaxValueValidator(5), MinValueValidator(0)]
    )

    pain = models.IntegerField(
        blank=True,
        default=1,
        validators=[MaxValueValidator(5), MinValueValidator(0)]
    )

    anxiety = models.IntegerField(
        blank=True,
        default=1,
        validators=[MaxValueValidator(5), MinValueValidator(0)]
    )

    seizures = models.IntegerField(
        blank=True,
        default=1,
        validators=[MaxValueValidator(5), MinValueValidator(0)]
    )

    rigidity = models.IntegerField(
        blank=True,
        default=1,
        validators=[MaxValueValidator(5), MinValueValidator(0)]
    )

    motivation = models.IntegerField(
        blank=True,
        default=1,
        validators=[MaxValueValidator(5), MinValueValidator(0)]
    )

    sleep = models.IntegerField(
        blank=True,
        default=1,
        validators=[MaxValueValidator(5), MinValueValidator(0)]
    )

    muscle_spasm = models.IntegerField(
        blank=True,
        default=1,
        validators=[MaxValueValidator(5), MinValueValidator(0)]
    )

    fatigue = models.IntegerField(
        blank=True,
        default=1,
        validators=[MaxValueValidator(5), MinValueValidator(0)]
    )

    hallucinations = models.IntegerField(
        blank=True,
        default=1,
        validators=[MaxValueValidator(5), MinValueValidator(0)]
    )

    constipation = models.IntegerField(
        blank=True,
        default=1,
        validators=[MaxValueValidator(5), MinValueValidator(0)]
    )


class PatientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.FileField(blank=True)
    content_type = models.CharField(max_length=50, blank=True)


    caregiver = models.ForeignKey(
        CaregiverProfile, on_delete=models.PROTECT, related_name='patient', null=True)
    doctor = models.ForeignKey(
        DoctorProfile, on_delete=models.PROTECT, related_name='patients', null=True)
    
    survey = models.ForeignKey(Survey, default=None, on_delete=models.PROTECT, null=True)




class CalendarEvent(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE, related_name='calendar_events')
    start = models.TimeField(auto_now_add=False, null=False)
    end = models.TimeField(auto_now_add=False, null=False)
    description = models.CharField(max_length=200, blank=True)
    date = models.DateField(auto_now_add=False, null=False)

    def __str__(self):
        return 'patient=' + self.patient.user.username + ', start=' + self.start.ToSting() + ', end=' + self.end.ToSting() + ', description=' + self.descriprion

