# Generated by Django 4.1.13 on 2024-05-30 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('description', models.TextField()),
            ],
            options={
                'db_table': 'medicines',
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'suppliers',
            },
        ),
        migrations.CreateModel(
            name='MedBatch',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('sold', models.IntegerField()),
                ('manufacture_date', models.DateField()),
                ('expiration_date', models.DateField()),
                ('received_date', models.DateField()),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicine.medicine')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicine.supplier')),
            ],
            options={
                'db_table': 'medicine_batch',
            },
        ),
    ]
