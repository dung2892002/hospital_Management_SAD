# Generated by Django 4.1.13 on 2024-05-29 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='blood_type',
        ),
    ]
