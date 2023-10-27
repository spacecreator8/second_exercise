from django import forms
from .models import *


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','surname','patronymic','username','email','password','agreement']


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ('name', 'description', 'category', 'photo' )

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['category'].empty_label = "Категория не выбрана"