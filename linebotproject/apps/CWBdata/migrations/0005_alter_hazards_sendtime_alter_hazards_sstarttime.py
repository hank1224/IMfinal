# Generated by Django 4.1.4 on 2022-12-16 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("CWBdata", "0004_alter_hazards_sphenomena"),
    ]

    operations = [
        migrations.AlterField(
            model_name="hazards",
            name="sEndTime",
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name="hazards",
            name="sStartTime",
            field=models.CharField(max_length=30, null=True),
        ),
    ]