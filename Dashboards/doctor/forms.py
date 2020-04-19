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


class SurveySettingForm(forms.Form):
    falls = forms.CharField(label="Falls", max_length=10, widget=forms.RadioSelect(
        choices=(
                ('True', 'True'),
                ('False', 'False')),
        attrs={'size': 20, 'id': 'id_falls', 'class': 'custom-control-input'}))

    depression = forms.CharField(label="Depression", max_length=10, widget=forms.RadioSelect(
        choices=(
                ('True', 'True'),
                ('False', 'False')),
        attrs={'id': 'id_depression', 'class': 'custom-control-input'}))

    dyskinesia = forms.CharField(label="Dyskinesia", max_length=10, widget=forms.RadioSelect(
        choices=(
                ('True', 'True'),
                ('False', 'False')),
        attrs={'id': 'id_dyskinesia', 'class': 'custom-control-input'}))

    movement = forms.CharField(label="Fine motor movement", max_length=10, widget=forms.RadioSelect(
        choices=(
                ('True', 'True'),
                ('False', 'False')),
        attrs={'id': 'id_movement', 'class': 'custom-control-input'}))

    thinking = forms.CharField(label="Thinking", max_length=10, widget=forms.RadioSelect(
        choices=(
                ('True', 'True'),
                ('False', 'False')),
        attrs={'id': 'id_thinking', 'class': 'custom-control-input'}))
    walking = forms.CharField(label="Walking", max_length=10, widget=forms.RadioSelect(
        choices=(
                ('True', 'True'),
                ('False', 'False')),
        attrs={'id': 'id_walking', 'class': 'custom-control-input'}))

    chest_pain = forms.CharField(label="Chest Pain or Palpitations", max_length=10, widget=forms.RadioSelect(
        choices=(
                ('True', 'True'),
                ('False', 'False')),
        attrs={'id': 'id_chest_pain', 'class': 'custom-control-input'}))

    tremor = forms.CharField(label="Tremor", max_length=10, widget=forms.RadioSelect(
        choices=(
                ('True', 'True'),
                ('False', 'False')),
        attrs={'id': 'id_tremor', 'class': 'custom-control-input'}))

    swallowing = forms.CharField(label="Swallowing", max_length=10, widget=forms.RadioSelect(
        choices=(
                ('True', 'True'),
                ('False', 'False')),
        attrs={'id': 'id_swallowing', 'class': 'custom-control-input'}))

    pain = forms.CharField(label="Pain", max_length=10, widget=forms.RadioSelect(
        choices=(
            ('True', 'True'),
            ('False', 'False')),
        attrs={'id': 'id_pain', 'class': 'custom-control-input'}))

    anxiety = forms.CharField(label="Anxiety", max_length=10, widget=forms.RadioSelect(
        choices=(
                ('True', 'True'),
                ('False', 'False')),
        attrs={'id': 'id_anxiety', 'class': 'custom-control-input'}))

    seizures = forms.CharField(label="Seizures", max_length=10, widget=forms.RadioSelect(
        choices=(
                ('True', 'True'),
                ('False', 'False')),
        attrs={'id': 'id_seizures', 'class': 'custom-control-input'}))

    rigidity = forms.CharField(label="Rigidity", max_length=10, widget=forms.RadioSelect(
        choices=(
                ('True', 'True'),
                ('False', 'False')),
        attrs={'id': 'id_rigidity', 'class': 'custom-control-input'}))

    motivation = forms.CharField(label="Motivation", max_length=10, widget=forms.RadioSelect(
        choices=(
                ('True', 'True'),
                ('False', 'False')),
        attrs={'id': 'id_motivation', 'class': 'custom-control-input'}))

    sleep = forms.CharField(label="Sleep", max_length=10, widget=forms.RadioSelect(
        choices=(
                ('True', 'True'),
                ('False', 'False')),
        attrs={'id': 'id_sleep', 'class': 'custom-control-input'}))

    muscle_spasm = forms.CharField(label="Muscle Spasm", max_length=10, widget=forms.RadioSelect(
        choices=(
                ('True', 'True'),
                ('False', 'False')),
        attrs={'id': 'id_muscle_spasm', 'class': 'custom-control-input'}))

    fatigue = forms.CharField(label="Fatigue", max_length=10, widget=forms.RadioSelect(
        choices=(
                ('True', 'True'),
                ('False', 'False')),
        attrs={'id': 'id_fatigue', 'class': 'custom-control-input'}))

    hallucinations = forms.CharField(label="Hallucinations", max_length=10, widget=forms.RadioSelect(
        choices=(
                ('True', 'True'),
                ('False', 'False')),
        attrs={'id': 'id_hallucinations', 'class': 'custom-control-input'}))
    
    constipation = forms.CharField(label="Constipation", max_length=10, widget=forms.RadioSelect(
        choices=(
                ('True', 'True'),
                ('False', 'False')),
        attrs={'id': 'id_constipation', 'class': 'custom-control-input'}))
