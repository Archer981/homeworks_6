from datetime import date, timedelta

from rest_framework.exceptions import ValidationError


def check_not_less_9_years(value: date):
    if date.today() - value < timedelta(days=3285):
        raise ValidationError('Age less than 9 years')


def check_email_not_rambler(value):
    if value.split('@')[1] == 'rambler.ru':
        raise ValidationError("Email can't be rambler.ru")
