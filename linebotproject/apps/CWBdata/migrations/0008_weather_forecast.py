# Generated by Django 3.2.5 on 2022-12-28 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CWBdata', '0007_rain'),
    ]

    operations = [
        migrations.CreateModel(
            name='weather_forecast',
            fields=[
                ('sLocationName', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('sWx', models.CharField(max_length=15, null=True)),
                ('sPop', models.FloatField()),
                ('sMinT', models.FloatField()),
                ('sMaxT', models.FloatField()),
                ('sCI', models.CharField(max_length=15, null=True)),
            ],
        ),
    ]
