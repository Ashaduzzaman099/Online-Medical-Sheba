# Generated by Django 4.2.16 on 2024-11-22 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine_store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price (TK)'),
        ),
    ]
