# Generated by Django 4.2.6 on 2023-11-01 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('b1', '0002_alter_user_password2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='agreement',
            field=models.BooleanField(blank=True, null=True, verbose_name='Согласие на обработку персоональных данных'),
        ),
    ]
