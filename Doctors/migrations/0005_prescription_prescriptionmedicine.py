# Generated by Django 4.2.11 on 2024-12-18 04:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Doctors', '0004_bookingrequest'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.PositiveIntegerField()),
                ('sex', models.CharField(max_length=10)),
                ('doctor_comment', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Doctors.appointment')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Doctors.doctorprofile')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PrescriptionMedicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('breakfast_dosage', models.BooleanField(default=False)),
                ('lunch_dosage', models.BooleanField(default=False)),
                ('dinner_dosage', models.BooleanField(default=False)),
                ('meal_remark', models.CharField(blank=True, choices=[('before', 'Before Meal'), ('after', 'After Meal')], max_length=10, null=True)),
                ('additional_notes', models.TextField(blank=True, null=True)),
                ('prescription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medicines', to='Doctors.prescription')),
            ],
        ),
    ]
