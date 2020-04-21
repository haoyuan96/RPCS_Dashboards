
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class RegistrationForm(UserCreationForm):
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
    user_type = forms.CharField(label="", max_length=10, widget=forms.RadioSelect(
        choices=(
            ('patient', 'Patient'),
            ('doctor', 'Doctor'),
            ('caregiver', 'Caregiver')),
        attrs={'id': 'id_user_type', 'class': 'custom-control-input'}))

    patient_username = forms.CharField(label="", max_length=20, widget=forms.TextInput(
        attrs={'placeholder': 'Patient Username', 'class': 'form-control form-control-user', 'id': 'id_patient_username'}))

    class Meta(UserCreationForm.Meta):
        model = User


class LoginForm(forms.Form):
    username = forms.CharField(label="", max_length=20, widget=forms.TextInput(
        attrs={'placeholder': 'Enter Username...', 'class': 'form-control form-control-user', 'id': 'id_username'}))
    password = forms.CharField(label="", max_length=200, widget=forms.PasswordInput(
        attrs={'placeholder': 'Password', 'class': 'form-control form-control-user', 'id': 'id_password'}))

    def clean(self):
        cleaned_data = super().clean()

        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError("Invalid Username/Password")
        return cleaned_data
