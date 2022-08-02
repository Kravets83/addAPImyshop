from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import BaseUser


class RegistrationForm(forms.ModelForm):
    user_name = forms.CharField(label='Enter User Name', min_length=4, max_length=50,
                                help_text='Required')
    email = forms.EmailField(max_length=100, help_text='Required',
                             error_messages={'Required': 'Not email'})
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_name'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Username'})
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'E-mail', 'name': 'email', 'id': 'id_email'})
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Repeat Password'})

    class Meta:
        model = BaseUser
        fields = ('user_name', 'email')

    def clean_user_name(self):
        user_name = self.cleaned_data['user_name'].lower()
        check = BaseUser.objects.filter(user_name=user_name)
        if check.count():
            raise forms.ValidationError('User name already exists')
        return user_name

    def clean_password2(self):
        clean_data = self.cleaned_data
        if clean_data['password'] != clean_data['password2']:
            raise forms.ValidationError('Password do not match!!!')
        return clean_data['password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if BaseUser.objects.filter(email=email).exists():
            raise forms.ValidationError('Email not valid')
        return email


class UserLoginForm(AuthenticationForm):

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Username', 'id': 'login-username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Password',
            'id': 'login-pwd',
        }
    ))

class UserEditForm(forms.ModelForm):

    email = forms.EmailField(
        label='Account email (can not be changed)', max_length=200, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'email', 'id': 'form-email', 'readonly': 'readonly'}))

    first_name = forms.CharField(
        label='Username', min_length=4, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Firstname', 'id': 'form-lastname'}))

    class Meta:
        model = BaseUser
        fields = ('email', 'first_name',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['email'].required = True
