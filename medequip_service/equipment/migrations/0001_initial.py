# Generated by Django 4.1.13 on 2024-05-30 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('quantity', models.IntegerField()),
                ('department_id', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'equipment',
            },
        ),
    ]
