# Generated by Django 4.2.6 on 2023-11-01 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('b1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password2',
            field=models.CharField(max_length=254, verbose_name='Повторите пароль'),
        ),
    ]