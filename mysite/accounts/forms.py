from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

    # specify the name of model to use 


class RegisterForm(UserCreationForm):

    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
