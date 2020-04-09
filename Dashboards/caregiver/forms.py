from django import forms

class CalendarEventForm(forms.Form):
    description = forms.CharField(label='Event', max_length=100, required = True)
    date = forms.DateField(widget=forms.HiddenInput())
    start_time = forms.TimeField(label='Start Time', required = True)
    end_time = forms.TimeField(label='End Time', required = True)
