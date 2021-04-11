from django.db import models
from client.models import Client


class Transaction(models.Model):
    owner = models.ForeignKey(Client, on_delete=models.CASCADE)
    date = models.DateTimeField()
    amount = models.IntegerField()

    PAYMENT_BY_MONEY = 'PBM'
    PAYMENT_BY_POINTS = 'PBP'
    ACCRUAL_POINTS = 'AP'

    TRANSACTION_TYPE = (
        (PAYMENT_BY_MONEY, 'Payment by money'),
        (PAYMENT_BY_POINTS, 'Payment by points'),
        (ACCRUAL_POINTS, 'Accrual points'),
    )
    type = models.CharField(max_length=3,
                            choices=TRANSACTION_TYPE,
                            default=ACCRUAL_POINTS)
