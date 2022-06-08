# Generated by Django 4.0.4 on 2022-06-06 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csw', '0011_education_and_training_certificates'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='education_and_training',
            name='certificates',
        ),
        migrations.AlterField(
            model_name='education_and_training',
            name='address',
            field=models.CharField(max_length=700, null=True, verbose_name='Address'),
        ),
    ]