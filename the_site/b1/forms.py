from django import forms
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

from .models import *




class RegistrationForm(forms.ModelForm):
    email = forms.EmailField()
    agreement = forms.BooleanField(required=True, label='Согласие на обработку пресоональных данных')
    class Meta:
        model = User
        fields = ['name','surname','patronymic','username','email','password','password2','agreement']
        widgets = {
            'name':forms.TextInput(attrs={ 'placeholder':'только кириллица'}),
            'surname':forms.TextInput(attrs={ 'placeholder':'только кириллица'}),
            'patronymic':forms.TextInput(attrs={ 'placeholder':'только кириллица'}),
            'password': forms.PasswordInput(attrs={'name': 'password','type': 'password', 'autocomplete': 'off',}),
            'password2': forms.PasswordInput(attrs={'name': 'password2','type': 'password', 'autocomplete': 'off', }),
        }
    def clean_name(self):
        ALLOWED_CHARS='йцукенгшщзхъэждлорпавыфячсмитьбюёЁЙЦУКЕНГШЩЗХЪЭЖДЛОРПАВЫФЯЧСМИТЬБЮ'
        name = self.cleaned_data['name']
        if not(set(name)) <= set(ALLOWED_CHARS):
            raise ValidationError("только кириллица")
        return name

    def clean_surname(self):
        ALLOWED_CHARS='йцукенгшщзхъэждлорпавыфячсмитьбюёЁЙЦУКЕНГШЩЗХЪЭЖДЛОРПАВЫФЯЧСМИТЬБЮ'
        surname = self.cleaned_data['surname']
        if not(set(surname))<= set(ALLOWED_CHARS):
            raise ValidationError("только кириллица")
        return surname

    def clean_patronymic(self):
        ALLOWED_CHARS='йцукенгшщзхъэждлорпавыфячсмитьбюёЁЙЦУКЕНГШЩЗХЪЭЖДЛОРПАВЫФЯЧСМИТЬБЮ'
        patronymic = self.cleaned_data['patronymic']
        if not(set(patronymic)) <= set(ALLOWED_CHARS):
            raise ValidationError("только кириллица")
        return patronymic


    # def clean_name(self):
    #     name = self.cleaned_data
    #     ALLOWED_CHARS="йцукенгшщзхъэждлорпавыфячсмитьбюёЙЦУКЕНГШЩЗХЪЭЖДЛОРПАВЫФЯЧСМИТЬБЮЁ"
    #     if not (set(name)) <= set(ALLOWED_CHARS):
    #         raise ValidationError("В имени может быть только кириллица.")
    #
    #     return name
    #
    # def clean_surname(self):
    #     surname = self.cleaned_data
    #     ALLOWED_CHARS="йцукенгшщзхъэждлорпавыфячсмитьбюёЙЦУКЕНГШЩЗХЪЭЖДЛОРПАВЫФЯЧСМИТЬБЮЁ"
    #     if not (set(surname)) <= set(ALLOWED_CHARS):
    #         raise ValidationError("В имени может быть только кириллица.")
    #
    #     return surname
    #
    # def clean_patronymic(self):
    #     patronymic = self.cleaned_data
    #     ALLOWED_CHARS="йцукенгшщзхъэждлорпавыфячсмитьбюёЙЦУКЕНГШЩЗХЪЭЖДЛОРПАВЫФЯЧСМИТЬБЮЁ"
    #     if not (set(patronymic)) <= set(ALLOWED_CHARS):
    #         raise ValidationError("В имени может быть только кириллица.")
    #
    #     return patronymic

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


STATUS_CHOISE_2 = [
        ('New', 'Новая'),
        ('Accepted', 'Принято в работу'),
        ('Finished', 'Выполнено'),
        ('All', 'Все заявки')
    ]
class FilterApplicationForm(forms.Form):
    status = forms.ChoiceField(choices=STATUS_CHOISE_2, label='Выберите статус', initial='All')


class CreateRealizationForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'cols': 40}), max_length=999,
                                  label='Описание проекта')
    class Meta:
        model = Realization
        fields = ['name','description','image']