# Generated by Django 4.2.16 on 2024-10-17 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('user', 'User'), ('doctor', 'Doctor')], default='user', max_length=10),
        ),
    ]
