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
