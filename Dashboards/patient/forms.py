from django import forms

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import PatientProfile
from django.forms.utils import ErrorList


class DivErrorList(ErrorList):
    def __str__(self):
        return self.as_divs()

    def as_divs(self):
        if not self:
            return ''
        return '<div class="invalid-tooltip">%s</div>' % ''.join(['<div class="invalid-tooltip">%s</div>' % e for e in self])


class LoginForm(forms.Form):
    username = forms.CharField(label="", max_length=20, widget=forms.TextInput(
        attrs={'placeholder': 'Username', 'class': 'form-control', 'id': 'id_username'}))
    password = forms.CharField(label="", max_length=200, widget=forms.PasswordInput(
        attrs={'placeholder': 'Password', 'class': 'form-control', 'id': 'id_password'}))

    # Customizes form validation for properties that apply to more
    # than one field.  Overrides the forms.Form.clean function.
    # def clean(self):
    #     # Calls our parent (forms.Form) .clean function, gets a dictionary
    #     # of cleaned data as a result
    #     cleaned_data = super().clean()

    #     # Confirms that the two password fields match
    #     username = cleaned_data.get('username')
    #     password = cleaned_data.get('password')
    #     user = authenticate(username=username, password=password)
    #     if not user:
    #         raise forms.ValidationError("Invalid username/password")

    #     # We must return the cleaned data we got from our parent.
    #     return cleaned_data


class RegistrationForm(UserCreationForm):
    error_css_class = 'invalid'
    username = forms.CharField(label="", max_length=20, widget=forms.TextInput(
        attrs={'placeholder': 'Username', 'class': 'form-control form-control-user', 'id': 'id_username'}))
    password1 = forms.CharField(label="", max_length=200, widget=forms.PasswordInput(
        attrs={'placeholder': 'Password', 'class': 'form-control form-control-user', 'id': 'id_password'}))
    password2 = forms.CharField(label="", max_length=200, widget=forms.PasswordInput(
        attrs={'placeholder': 'Confirm', 'class': 'form-control form-control-user', 'id': 'id_confirm_password'}))
    email = forms.CharField(label="", max_length=50,
                            widget=forms.EmailInput(attrs={'placeholder': 'E-mail', 'class': 'form-control form-control-user', 'id': 'id_email'}))
    first_name = forms.CharField(label="", max_length=20, widget=forms.TextInput(
        attrs={'placeholder': 'First Name', 'class': 'form-control form-control-user', 'id': 'id_first_name'}))
    last_name = forms.CharField(label="", max_length=20, widget=forms.TextInput(
        attrs={'placeholder': 'Last Name', 'class': 'form-control form-control-user', 'id': 'id_last_name'}))

    class Meta(UserCreationForm.Meta):
        model = User

    # Customizes form validation for properties that apply to more
    # than one field.  Overrides the forms.Form.clean function.
    # def clean(self):
    #     # Calls our parent (forms.Form) .clean function, gets a dictionary
    #     # of cleaned data as a result
    #     cleaned_data = super().clean()

    #     # Confirms that the two password fields match
    #     password1 = cleaned_data.get('password1')
    #     password2 = cleaned_data.get('password2')
    #     if password1 and password2 and password1 != password2:
    #         raise forms.ValidationError("Passwords did not match.")

    #     # We must return the cleaned data we got from our parent.
    #     return cleaned_data

    # Customizes form validation for the username field.

    # def clean_username(self):
    #     # Confirms that the username is not already present in the
    #     # User model database.
    #     username = self.cleaned_data.get('username')
    #     if User.objects.filter(username__exact=username):
    #         raise forms.ValidationError("Username is already taken.")

    #     # We must return the cleaned data we got from the cleaned_data
    #     # dictionary
    #     return username


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
