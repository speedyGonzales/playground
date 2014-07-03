from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm


from .models import SignUp


class UserForm(ModelForm):
    ''''
    form for user login
    '''
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'password']


class RegisterForm(UserCreationForm):
    '''
    form for user registration, use django's UserCreationForm
    '''
    email = forms.EmailField(label='E-mail')
    first_name = forms.CharField(label='First name', required=False)
    last_name = forms.CharField(label='Last name', required=False)

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']



