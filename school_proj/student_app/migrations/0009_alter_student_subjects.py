# Generated by Django 5.0.3 on 2024-03-22 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0008_student_subjects'),
        ('subject_app', '0004_remove_subject_students'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='subjects',
            field=models.ManyToManyField(related_name='subjects', to='subject_app.subject'),
        ),
    ]
