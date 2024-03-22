# from django.db import models
# from django.core import validators as v
# from .validators import (
#     validate_combination_format,
#     validate_name_format,
#     validate_school_email,
# )
# from subject_app.models import Subject

# # Create your models here.
# class Student(models.Model):
#     name = models.CharField(
#         max_length=255, null=False, blank=False, validators=[validate_name_format]
#     )
#     student_email = models.EmailField(
#         null=False, blank=False, unique=True, validators=[validate_school_email]
#     )
#     personal_email = models.EmailField(null=False, blank=False, unique=True)
#     locker_number = models.IntegerField(
#         default=110,
#         null=False,
#         blank=False,
#         unique=True,
#         validators=[v.MinValueValidator(1), v.MaxValueValidator(200)],
#     )
#     locker_combination = models.CharField(
#         default="12-12-12",
#         null=False,
#         blank=False,
#         max_length=255,
#         validators=[validate_combination_format],
#     )
#     good_student = models.BooleanField(default=True)
#     subjects = models.ManyToManyField(Subject, related_name='students')

#     def add_subject(self, subject_id):
#         subject_length = self.subjects.count()
#         if subject_length < 8:
#             self.subjects.add(subject_id)
#         else:
#             raise Exception("This students class schedule is full!")
        
#     def remove_subject(self, subject_id):
#         subject_length = self.subjects.count()
#         if subject_length > 0:
#             self.subjects.remove(subject_id)
#         else:
#             raise Exception("This students class schedule is empty!")


from django.db import models
from django.core import validators as v
from .validators import validate_name_format
from .validators import validate_combination_format
from .validators import validate_school_email
# from subject_app.models import Subject
# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=50, null=False,
                            unique=False, validators=[validate_name_format])  # Regex Validator
    student_email = models.EmailField(
        max_length=100, null=False, unique=True, validators=[validate_school_email])  # Regex validator
    personal_email = models.EmailField(
        max_length=100, null=True, unique=True)  # No validator
    locker_number = models.IntegerField(null=False, unique=True, default=110, validators=[
                                        v.MaxValueValidator(200), v.MinValueValidator(1)])  # MinVal/MaxVal validators
    locker_combination = models.CharField(
        null=False, unique=False, default='12-12-12', validators=[v.MaxLengthValidator(8), validate_combination_format])  # Regex validator
    good_student = models.BooleanField(
        null=False, unique=False, default=True)  # No validator
    subjects = models.ManyToManyField(
        'subject_app.Subject', related_name='subjects', unique=False)

    def __str__(self):
        return f'{self.name} - {self.student_email} - {self.locker_number}'

    def newLockerNumber(self, num):
        self.locker_number = num
        self.save()

    def changeStatus(self, bool):
        self.good_student = bool
        self.save()

    def add_subject(self, subj_pk):
        if self.subjects.count() < 8:
            self.subjects.add(subj_pk)
        else: 
            raise Exception("This students class schedule is full!")
    def remove_subject(self, subj_pk):
        if self.subjects.count() > 0:
            self.subjects.remove(subj_pk)
        else:
            raise Exception("This students class schedule is empty!")