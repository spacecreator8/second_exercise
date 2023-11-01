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
    password2 = models.CharField(max_length=254, verbose_name='Повторите пароль', blank=False)
    agreement = models.BooleanField(verbose_name='Согласие на обработку персоональных данных', blank=True,
                                    null=True)
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
    photo = models.ImageField( verbose_name='Проект помещения', upload_to=get_name_file, blank=True, null=True,
                              validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])])

    # STATUS_CHOISE = [
    #     ('New', 'Новая'),
    #     ('Accepted', 'Принято в работу'),
    #     ('Finished', 'Выполнено')
    # ]choices=STATUS_CHOISE

    status = models.CharField(max_length=254, verbose_name='Статус', default='New')
    date_creation = models.DateTimeField(auto_now_add=True, null=True)
    username = models.CharField(max_length=254, verbose_name='Логин', blank=True, null=True, db_column='username_application')
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
    description = models.CharField(max_length=999,verbose_name='Описание', blank=False)
    image = models.ImageField( upload_to=get_name_file, blank=True, null=True,
                              validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])])
    date_execution = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.name)
