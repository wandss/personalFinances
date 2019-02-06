from django.db import models


class ExpenseType(models.Model):
    label = models.CharField(max_length=50)
    dt_creation = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.label

    class Meta:
        ordering = ['label']
        unique_together = ('label', 'created_by')


class OperationType(models.Model):
    label = models.CharField(max_length=10)
    dt_creation = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.label

    class Meta:
        ordering = ['label']


class Transactions(models.Model):
    expense = models.ForeignKey(ExpenseType, related_name='expenses',
                                on_delete=models.PROTECT)
    operation_type = models.ForeignKey(OperationType,
                                       related_name='operationtype',
                                       on_delete=models.PROTECT)
    estabelecimento = models.CharField('Establishment', max_length=50)
    amount = models.DecimalField('Value', max_digits=9, decimal_places=2)
    dt_transaction = models.DateTimeField('Transaction Date')
    dt_creation = models.DateTimeField(auto_now=True)
    info = models.CharField(max_length=100, blank=True, null=True)
    parcels = models.IntegerField(default=0)
    created_by = models.ForeignKey('auth.user', on_delete=models.CASCADE)

    def __str__(self):
        return self.estabelecimento

    # return "{}-{}".format(self.estabelecimento, self.expense)

    class Meta:
        ordering = ['-dt_transaction']
        verbose_name_plural = "Transactions"
