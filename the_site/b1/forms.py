from django import forms
from .models import *


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','surname','patronymic','username','email','password','agreement']