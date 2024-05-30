# Generated by Django 4.1.13 on 2024-05-30 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalService',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('description', models.TextField()),
                ('department_id', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'medical_service',
            },
        ),
    ]