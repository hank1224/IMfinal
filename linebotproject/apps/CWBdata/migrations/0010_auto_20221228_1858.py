# Generated by Django 3.2.5 on 2022-12-28 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CWBdata', '0009_river'),
    ]

    operations = [
        migrations.AddField(
            model_name='river',
            name='sRecordTime',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='river',
            name='sWaterLevel',
            field=models.FloatField(null=True),
        ),
    ]