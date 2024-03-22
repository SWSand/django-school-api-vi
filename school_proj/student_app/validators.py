# from django.core.exceptions import ValidationError
# import re

# def validate_name_format(value):
#     """
#     Validator for the "First M. Last" name format.
#     """
#     name_pattern = re.compile(r'^[A-Za-z]+ [A-Za-z]\. [A-Za-z]+$')
#     if not name_pattern.match(value):
#         raise ValidationError('Name must be in the format "First Middle Initial. Last"')

# def validate_school_email(value):
#     """
#     Validator for the school email format ending with "@school.com".
#     """
#     email_pattern = re.compile(r'^.+@school\.com$')
#     if not email_pattern.match(value):
#         raise ValidationError('Invalid school email format. Please use an email ending with "@school.com".')

# def validate_combination_format(value):
#     """
#     Validator for the format "12-12-12" (ensures there are numbers only).
#     """
#     combination_pattern = re.compile(r'^\d{2}-\d{2}-\d{2}$')
#     if not combination_pattern.match(value):
#         raise ValidationError('Combination must be in the format "12-12-12"')



from django.core.exceptions import ValidationError
import re


def validate_name_format(name):
    error_message = 'Name must be in the format "First Middle Initial. Last"'
    # regex format: "First M. Last"
    regex = r'^[A-Z][a-z]+ [A-Z]\. [A-Z][a-z]+$'
    good_name = re.match(regex, name)
    if good_name:
        return name
    else:
        raise ValidationError(error_message, params={'name': name})


def validate_school_email(email):
    error_message = 'Invalid school email format. Please use an email ending with "@school.com".'
    # regex format: ends with "@school.com"
    regex = r'^[a-z0-9A-Z._%+-]+@school\.com$'
    good_email = re.match(regex, email)
    if good_email:
        return email
    else:
        raise ValidationError(error_message, params={'student_email': email})


def validate_combination_format(combo):
    error_message = 'Combination must be in the format "12-12-12"'
    # regex format: "##-##-##"
    regex = r'^[0-9]{2}-[0-9]{2}-[0-9]{2}$'
    good_combo = re.match(regex, combo)
    if good_combo:
        return combo
    else:
        raise ValidationError(error_message, params={
                              'locker_combination': combo})