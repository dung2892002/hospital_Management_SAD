# Generated by Django 4.1.13 on 2024-05-29 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('no_house', models.CharField(max_length=10)),
                ('street', models.CharField(max_length=50)),
                ('ward', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('province', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'addresses',
            },
        ),
        migrations.CreateModel(
            name='Blood',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'bloods',
            },
        ),
        migrations.CreateModel(
            name='Fullname',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'fullnames',
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('mobile_number', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('blood_type', models.CharField(max_length=3)),
                ('allergies', models.TextField(blank=True, null=True)),
                ('medical_history', models.TextField(blank=True, null=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.address')),
                ('blood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.blood')),
                ('fullname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.fullname')),
            ],
            options={
                'db_table': 'patients',
            },
        ),
    ]
