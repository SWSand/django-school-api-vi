# from django.core.exceptions import ValidationError
# import re


# def validate_subject_format(value):
#     if value.title() != value:
#         raise ValidationError("Subject must be in title case format.")


# def validate_professor_name(value):
#     """
#     Validator for ensuring the format "Professor [Name]" with capitalized first letters.
#     """
#     # Split the input value into words
#     words = value.split()

#     # Check if there are at least two words
#     if len(words) < 2:
#         raise ValidationError('Professor name must be in the format "Professor Adam".')

#     # Check if the first word is "Professor" and the second word starts with an uppercase letter
#     if words[0] != "Professor" or words[1].title() != words[1]:
#         raise ValidationError('Professor name must be in the format "Professor Adam".')


from django.core.exceptions import ValidationError
import re


def validate_subject_format(subject):
    error_message = "Subject must be in title case format."
    regex = r'^[A-Z][a-z]+[ [A-Za-z][a-z]*]*$'
    good_subject = re.match(regex, subject)
    if good_subject:
        return subject
    else:
        raise ValidationError(error_message)


def validate_professor_name(name):
    error_message = 'Professor name must be in the format "Professor Adam".'
    regex = r'^[A-Z][a-z\.]+[ [A-Z][a-z]*]*$'
    good_name = re.match(regex, name)
    if good_name:
        return name
    else:
        raise ValidationError(error_message)