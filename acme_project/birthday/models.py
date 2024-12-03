from django.db import models
from django.utils import timezone
from .validators import real_age

# class Birthday(models.Model):
#     first_name = models.CharField('Имя', max_length=20)
#     last_name = models.CharField(
#         'Фамилия', blank=True, help_text='Необязательное поле', max_length=20
#     )
#     birthday = models.DateField('Дата рождения')
#     registration_date = models.DateTimeField('Дата регистрации', default=timezone.now)

class Birthday(models.Model):
    first_name = models.CharField('Имя', max_length=20)
    last_name = models.CharField(
        'Фамилия', max_length=20, help_text='Необязательное поле', blank=True
    )
    # Валидатор указывается в описании поля.
    birthday = models.DateField('Дата рождения', validators=(real_age,))
    registration_date = models.DateTimeField('Дата регистрации', default=timezone.now) 