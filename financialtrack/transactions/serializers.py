from rest_framework.serializers import ModelSerializer, SerializerMethodField
from transactions.models import ExpenseType, Transactions, OperationType

class ExpenseTypeSerializer(ModelSerializer):
    username = SerializerMethodField()
    class Meta:
        model = ExpenseType
        fields = ('id','label','dt_creation', 'username')

    def get_username(self, obj):
        return obj.created_by.username

class OperationTypeSerializer(ModelSerializer):
    class Meta:
        model = OperationType
        fields = ('id', 'label')

class TransactionsSerializer(ModelSerializer):
    operation_type_label = SerializerMethodField()
    expense_label = SerializerMethodField()

    class Meta:
        model = Transactions
        fields = ('id','estabelecimento',
                  'amount','dt_transaction','info',
                  'parcels','expense', 'operation_type',
                  'operation_type_label', 'expense_label'
                 )
    def get_operation_type_label(self, obj):
        return obj.operation_type.label

    def get_expense_label(self, obj):
        return obj.expense.label


