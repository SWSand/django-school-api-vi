# Generated by Django 5.0.3 on 2024-03-22 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subject_app', '0003_subject_students_alter_subject_professor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='students',
        ),
    ]