from django import forms
from tempus_dominus.widgets import DatePicker, TimePicker

class DoctorCalendarEventForm(forms.Form):
    description = forms.CharField(label='Event', max_length=100, required=True)
    patient = forms.CharField(label='Patient Username', max_length=100, required=False)
    date = forms.DateField(widget=forms.HiddenInput())
    start_time = forms.TimeField(label='Start Time', widget=TimePicker(
        options={
            'format': 'HH:mm',
            'useCurrent': True
        }
    ), required=True)
    end_time = forms.TimeField(label='End Time', widget=TimePicker(
        options={
            'format': 'HH:mm',
            'useCurrent': True
        }
    ), required=True)
