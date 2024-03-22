# Generated by Django 5.0.3 on 2024-03-22 19:01

import django.core.validators
import student_app.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0006_student_subjects'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='subjects',
        ),
        migrations.AlterField(
            model_name='student',
            name='locker_combination',
            field=models.CharField(default='12-12-12', validators=[django.core.validators.MaxLengthValidator(8), student_app.validators.validate_combination_format]),
        ),
        migrations.AlterField(
            model_name='student',
            name='locker_number',
            field=models.IntegerField(default=110, unique=True, validators=[django.core.validators.MaxValueValidator(200), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=50, validators=[student_app.validators.validate_name_format]),
        ),
        migrations.AlterField(
            model_name='student',
            name='personal_email',
            field=models.EmailField(max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_email',
            field=models.EmailField(max_length=100, unique=True, validators=[student_app.validators.validate_school_email]),
        ),
    ]