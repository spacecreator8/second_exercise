# Generated by Django 4.2.6 on 2023-10-27 03:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('b1', '0003_alter_user_agreement_alter_user_applications'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='suggestions',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='b1.realization', verbose_name='Предложения реализации'),
        ),
    ]
