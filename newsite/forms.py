from django import forms
from django.forms import PasswordInput, TextInput
from django.contrib.auth.models import User


class UserRegForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name',)
        widgets = {
            'password': PasswordInput(),

        }


class UserLogForm(forms.Form):
    username = forms.CharField(max_length=50, label='Имя пользователя')
    password = forms.CharField(
        max_length=50, widget=PasswordInput(), label='Пароль')

    class Meta:
        model = User
