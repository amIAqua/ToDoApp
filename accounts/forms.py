from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class UserRegistrationForm(UserCreationForm):

    first_name = forms.CharField(max_length  = 40)
    last_name = forms.CharField(max_length  = 50)
    email = forms.EmailField(required = False)

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2',
            ]
        