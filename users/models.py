from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.db.models import TextChoices

from users.validators import check_not_less_9_years, check_email_not_rambler


class UserRoles(TextChoices):
    MEMBER = 'member', 'Пользователь'
    ADMIN = 'admin', 'Админ'
    MODERATOR = 'moderator', 'Модератор'


class User(AbstractUser):
    age = models.PositiveSmallIntegerField(null=True, blank=True)
    locations = models.ManyToManyField('Location')
    role = models.CharField(max_length=9, choices=UserRoles.choices, default=UserRoles.MEMBER)
    birth_date = models.DateField(null=True, blank=True, validators=[check_not_less_9_years])
    email = models.EmailField(validators=[RegexValidator(
        regex='rambler.ru',
        message='Выберите другой домен',
        inverse_match=True
    )], unique=True)
    # email = models.EmailField(max_length=100, validators=[check_email_not_rambler])

    def save(self, *args, **kwargs):
        self.set_password(raw_password=self.password)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Location(models.Model):
    name = models.CharField(max_length=200, unique=True)
    lat = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    lng = models.DecimalField(max_digits=9, decimal_places=6, null=True)

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'

    def __str__(self):
        return self.name


# class User(models.Model):
#     first_name = models.CharField(max_length=200)
#     last_name = models.CharField(max_length=200)
#     username = models.CharField(max_length=200)
#     password = models.CharField(max_length=200)
#     role = models.CharField(max_length=9, choices=UserRoles.choices, default=UserRoles.MEMBER)
#     age = models.PositiveSmallIntegerField()
#     locations = models.ManyToManyField('Location')
#
#     class Meta:
#         verbose_name = 'Пользователь'
#         verbose_name_plural = 'Пользователи'
#
#     def __str__(self):
#         return self.username
#
#     def serialize(self):
#         return {
#             'id': self.id,
#             'first_name': self.first_name,
#             'last_name': self.last_name,
#             'username': self.username,
#             'password': self.password,
#             'role': self.role,
#             'age': self.age,
#             'locations': [loc.name for loc in self.locations.all()],
#         }
