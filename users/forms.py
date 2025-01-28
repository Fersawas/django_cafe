from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=150,
                             required=True,
                             help_text='Input your email')
    
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2'
        )


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='username')
    password = forms.CharField(label='password')