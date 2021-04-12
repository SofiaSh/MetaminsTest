from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class Client(AbstractUser):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    card_number_regex = RegexValidator(regex=r'[0-9]{16}',
                                       message='Wrong card number')
    card_number = models.CharField(validators=[card_number_regex], max_length=16)

    balance = models.IntegerField(default=0)

    def __str__(self):
        return self.username