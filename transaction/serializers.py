from .models import Transaction
from rest_framework import serializers


class TransactionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Transaction
        fields = ('first_name', 'last_name' 'phone_number', 'balance', 'card_number')
