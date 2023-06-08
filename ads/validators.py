from rest_framework.exceptions import ValidationError


def is_not_published(value):
    if value:
        raise ValidationError("Status can't be published")
