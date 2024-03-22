# Generated by Django 5.0.3 on 2024-03-22 15:30

import subject_app.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subject_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='professor',
            field=models.CharField(validators=[subject_app.validators.validate_professor_name]),
        ),
        migrations.AlterField(
            model_name='subject',
            name='subject_name',
            field=models.CharField(unique=True, validators=[subject_app.validators.validate_subject_format]),
        ),
    ]
