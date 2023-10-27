from django.core.validators import FileExtensionValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.crypto import get_random_string


class User(AbstractUser):
    name = models.CharField(max_length=254, verbose_name='Имя', blank=False)
    surname = models.CharField(max_length=254, verbose_name='Фамилия', blank=False)
    patronymic = models.CharField(max_length=254, verbose_name='Отчество', blank=True)
    username = models.CharField(max_length=254, verbose_name='Логин', unique=True, blank=False)
    email = models.CharField(max_length=254, verbose_name='Почта', unique=True, blank=False)
    password = models.CharField(max_length=254, verbose_name='Пароль', blank=False)
    agreement = models.BooleanField(verbose_name='Согласие на обработку персоональных данных', blank=False,
                                    default=True)
    date_execution = models.DateTimeField(auto_now_add=True, null=True)
    applications = models.ForeignKey('Application', on_delete=models.CASCADE, verbose_name='Заявки', null=True,
                                     related_name='user', blank=True)

    USERNAME_FIELD = 'username'

    def full_name(self):
        return self.surname + ' ' + self.name + ' ' + self.patronymic

    def __str__(self):
        return self.username


def get_name_file(instance, filename):
    return '/'.join([get_random_string(length=5) + '_' + filename])


class Application(models.Model):
    name = models.CharField(max_length=254, verbose_name='Имя заявки', blank=True, null=True)
    description = models.CharField(max_length=254, verbose_name='Описание', blank=False)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория желаемого стиля',
                                 blank=False)
    photo = models.ImageField(max_length=254, verbose_name='Проект помещения', upload_to=get_name_file, blank=True,
                              validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])])

    STATUS_CHOISE = [
        ('Accepted', 'Принято в работу'),
        ('Finished', 'Выполнено')
    ]

    status = models.CharField(max_length=254, verbose_name='Статус', choices=STATUS_CHOISE, default='Accepted')
    suggestions = models.ForeignKey('Realization', on_delete=models.CASCADE, verbose_name='Предложения реализации',
                                    blank=True, null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=254, verbose_name='Название категории', blank=False)

    def __str__(self):
        return self.name


class Realization(models.Model):
    name = models.CharField(max_length=254, verbose_name='Название', blank=False,)
    description = models.CharField(max_length=254, verbose_name='Описание', blank=False)
    image = models.ImageField(max_length=254, upload_to=get_name_file, blank=True,
                              validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])])
    date_execution = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.name)
