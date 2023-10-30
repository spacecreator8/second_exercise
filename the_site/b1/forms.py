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


class DoYouWantDel(forms.Form):
    CHOICES = [
        ('yes','Да, удалить'),
        ('no', 'Нет'),
    ]
    sure = forms.ChoiceField(widget=forms.RadioSelect, choices = CHOICES)


STATUS_CHOISE = [
        ('New', 'Новая'),
        ('Accepted', 'Принято в работу'),
        ('Finished', 'Выполнено')
    ]

class ApplProcessingForm(forms.ModelForm):
    username = forms.CharField(max_length=50, disabled=True, label='Имя пользователя', required=False)
    name = forms.CharField(max_length=50, disabled=True,label='Имя заявки')
    category = forms.ModelChoiceField(queryset=Category.objects.all() ,disabled=True,label='Стиль оформления')
    description = forms.CharField(widget= forms.Textarea(attrs={'rows': 10, 'cols': 40}),max_length=50, disabled=True,label='Описание, требования')
    photo = forms.ImageField(disabled='True',label='Проект помещения', required=False)
    status = forms.ChoiceField(choices=STATUS_CHOISE)
    class Meta:
        model = Application
        fields = ['username','name','category', 'description','photo','status','suggestions']




