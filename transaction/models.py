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

    def save(self, *args, **kwargs):
        super(Transaction, self).save(*args, **kwargs)
        owner = Client.objects.get(card_number=self.owner)

        if self.ACCRUAL_POINTS == self.type:
            owner.balance += self.amount
            owner.save()
        elif self.PAYMENT_BY_POINTS == self.type:
            owner.balance -= self.amount
            owner.save()
