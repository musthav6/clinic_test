# Generated by Django 4.2.13 on 2024-06-25 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ai_clinic_proj', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.DeleteModel(
            name='Teams',
        ),
    ]