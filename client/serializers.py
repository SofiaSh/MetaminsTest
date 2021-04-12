from .models import Client
from rest_framework import serializers
from transaction.serializers import TransactionSerializer


class ClientSerializer(serializers.ModelSerializer):
    transaction = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='transaction-detail'
    )

    class Meta:
        model = Client
        fields = ('first_name', 'last_name', 'phone_number',
                  'balance', 'card_number', 'password', 'transaction')
