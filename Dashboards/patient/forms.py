from django import forms

from .models import PatientProfile
from django.forms.utils import ErrorList


class DivErrorList(ErrorList):
    def __str__(self):
        return self.as_divs()

    def as_divs(self):
        if not self:
            return ''
        return '<div class="invalid-tooltip">%s</div>' % ''.join(['<div class="invalid-tooltip">%s</div>' % e for e in self])


class PatientProfileForm(forms.ModelForm):
    class Meta:
        model = PatientProfile
        fields = ('picture',)
        widgets = {
            'picture': forms.FileInput(attrs={'class': 'form-control-file', 'id': 'id_profile_picture'}),
        }
        labels = {
            'picture': "Upload image",
        }

    def clean_picture(self):
        picture = self.cleaned_data['picture']
        if not picture:
            raise forms.ValidationError('You must upload a picture')
        if not picture.content_type or not picture.content_type.startswith('image'):
            raise forms.ValidationError('File type is not image')
        if picture.size > MAX_UPLOAD_SIZE:
            raise forms.ValidationError(
                'File too big (max size is {0} bytes)'.format(MAX_UPLOAD_SIZE))
        return picture
        
class SurveyForm(forms.Form):
    falls = forms.CharField(label="Falls", max_length=10, widget=forms.RadioSelect(
        choices=(
                ('0', '0'),
                ('1', '1'),
                ('2', '2'),
                ('3', '3'),
                ('4', '4'),
                ('5', '5')),
        attrs={'size': 20, 'id': 'id_falls', 'class': 'custom-control-input'}))

    depression = forms.CharField(label="Depression", max_length=10, widget=forms.RadioSelect(
        choices=(
                ('0', '0'),
                ('1', '1'),
                ('2', '2'),
                ('3', '3'),
                ('4', '4'),
                ('5', '5')),
        attrs={'id': 'id_depression', 'class': 'custom-control-input'}))

    dyskinesia = forms.CharField(label="Dyskinesia", max_length=10, widget=forms.RadioSelect(
        choices=(
                ('0', '0'),
                ('1', '1'),
                ('2', '2'),
                ('3', '3'),
                ('4', '4'),
                ('5', '5')),
        attrs={'id': 'id_dyskinesia', 'class': 'custom-control-input'}))

    movement = forms.CharField(label="Fine motor movement", max_length=10, widget=forms.RadioSelect(
        choices=(
                ('0', '0'),
                ('1', '1'),
                ('2', '2'),
                ('3', '3'),
                ('4', '4'),
                ('5', '5')),
        attrs={'id': 'id_movement', 'class': 'custom-control-input'}))

    thinking = forms.CharField(label="Thinking", max_length=10, widget=forms.RadioSelect(
        choices=(
                ('0', '0'),
                ('1', '1'),
                ('2', '2'),
                ('3', '3'),
                ('4', '4'),
                ('5', '5')),
        attrs={'id': 'id_thinking', 'class': 'custom-control-input'}))
    walking = forms.CharField(label="Walking", max_length=10, widget=forms.RadioSelect(
        choices=(
            ('0', '0'),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5')),
        attrs={'id': 'id_walking', 'class': 'custom-control-input'}))

    chest_pain = forms.CharField(label="Chest Pain or Palpitations", max_length=10, widget=forms.RadioSelect(
        choices=(
            ('0', '0'),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5')),
        attrs={'id': 'id_chest_pain', 'class': 'custom-control-input'}))

    tremor = forms.CharField(label="Tremor", max_length=10, widget=forms.RadioSelect(
        choices=(
            ('0', '0'),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5')),
        attrs={'id': 'id_tremor', 'class': 'custom-control-input'}))

    swallowing = forms.CharField(label="Swallowing", max_length=10, widget=forms.RadioSelect(
        choices=(
                ('0', '0'),
                ('1', '1'),
                ('2', '2'),
                ('3', '3'),
                ('4', '4'),
                ('5', '5')),
        attrs={'id': 'id_swallowing', 'class': 'custom-control-input'}))

    pain = forms.CharField(label="Pain", max_length=10, widget=forms.RadioSelect(
        choices=(
            ('0', '0'),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5')),
        attrs={'id': 'id_pain', 'class': 'custom-control-input'}))

    anxiety = forms.CharField(label="Anxiety", max_length=10, widget=forms.RadioSelect(
        choices=(
            ('0', '0'),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5')),
        attrs={'id': 'id_anxiety', 'class': 'custom-control-input'}))

    seizures = forms.CharField(label="Seizures", max_length=10, widget=forms.RadioSelect(
        choices=(
            ('0', '0'),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5')),
        attrs={'id': 'id_seizures', 'class': 'custom-control-input'}))

    rigidity = forms.CharField(label="Rigidity", max_length=10, widget=forms.RadioSelect(
        choices=(
            ('0', '0'),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5')),
        attrs={'id': 'id_rigidity', 'class': 'custom-control-input'}))

    motivation = forms.CharField(label="Motivation", max_length=10, widget=forms.RadioSelect(
        choices=(
            ('0', '0'),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5')),
        attrs={'id': 'id_motivation', 'class': 'custom-control-input'}))

    sleep = forms.CharField(label="Sleep", max_length=10, widget=forms.RadioSelect(
        choices=(
            ('0', '0'),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5')),
        attrs={'id': 'id_sleep', 'class': 'custom-control-input'}))

    muscle_spasm = forms.CharField(label="Muscle Spasm", max_length=10, widget=forms.RadioSelect(
        choices=(
            ('0', '0'),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5')),
        attrs={'id': 'id_muscle_spasm', 'class': 'custom-control-input'}))

    fatigue = forms.CharField(label="Fatigue", max_length=10, widget=forms.RadioSelect(
        choices=(
            ('0', '0'),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5')),
        attrs={'id': 'id_fatigue', 'class': 'custom-control-input'}))

    hallucinations = forms.CharField(label="Hallucinations", max_length=10, widget=forms.RadioSelect(
        choices=(
            ('0', '0'),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5')),
        attrs={'id': 'id_hallucinations', 'class': 'custom-control-input'}))
    constipation = forms.CharField(label="Constipation", max_length=10, widget=forms.RadioSelect(
        choices=(
            ('0', '0'),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5')),
        attrs={'id': 'id_constipation', 'class': 'custom-control-input'}))
