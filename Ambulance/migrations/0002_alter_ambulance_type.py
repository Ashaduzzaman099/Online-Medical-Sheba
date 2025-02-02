# Generated by Django 4.2.16 on 2024-11-30 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ambulance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ambulance',
            name='type',
            field=models.CharField(choices=[('AC', 'AC Ambulance Service'), ('Non-AC', 'Non-AC Ambulance Service'), ('ALS', 'ALS Ambulance Service'), ('ACLS', 'ACLS Ambulance Service'), ('AIR', 'AIR Ambulance Service'), ('ICU', 'ICU Ambulance Service'), ('NICU', 'NICU Ambulance Service'), ('Freezing', 'Freezing Ambulance Service')], max_length=20),
        ),
    ]
