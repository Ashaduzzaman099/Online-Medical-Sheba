# Generated by Django 4.2.11 on 2024-12-18 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doctors', '0005_prescription_prescriptionmedicine'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescription',
            name='sex',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
