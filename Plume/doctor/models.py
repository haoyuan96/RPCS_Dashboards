from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class DoctorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.FileField(blank=True)
    content_type = models.CharField(max_length=50, blank=True)

    # office_address = models.CharField(max_length=50)
    # phone = models.CharField(max_length=20)
    # working_time_from = models.TimeField(_(u"Conversation Time"), auto_now_add=True, blank=True)
    # working_time_to = models.TimeField(_(u"Conversation Time"), auto_now_add=True, blank=True)

    # def __str__(self):
    # return 'id=' + str(self.id) + ',patients="' + self.patients.all() + '"'

class DoctorCalendarEvent(models.Model):
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE, related_name='calendar_events')
    start = models.TimeField(auto_now_add=False, null=False)
    end = models.TimeField(auto_now_add=False, null=False)
    description = models.CharField(max_length=200, blank=True)
    date = models.DateField(auto_now_add=False, null=False)

    def __str__(self):
        return 'doctor=' + self.patient.user.username + ', start=' + self.start.ToSting() + ', end=' + self.end.ToSting() + ', description=' + self.descriprion

