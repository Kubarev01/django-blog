
from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm, UserChangeForm

from users.models import User


class UserSignUpForm(AuthenticationForm):
    class Meta:
        model=User
        fields=(
            'username',
            'password'

        )

    username=forms.CharField()
    password=forms.CharField()


class UserRegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=(
            'username',
            'email',
            'password1',
            'password2'
        )

    username=forms.CharField()
    email=forms.EmailField()
    password1=forms.CharField()
    password2=forms.CharField()