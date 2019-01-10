from rest_framework.serializers import (ModelSerializer, 
        SerializerMethodField)
from transactions.models import Transactions

class ExpenseTypeTransactionsSerializer(ModelSerializer):
    class Meta:
        model = Transactions
        fields = ('id', 'dt_transaction', 'amount')
