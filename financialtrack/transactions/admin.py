from django.contrib import admin
from transactions.models import ExpenseType, Transactions, OperationType

class ExpenseTypeAdmin(admin.ModelAdmin):
    list_filter = ['created_by']
    list_display = ['label', 'dt_creation', 'created_by']

admin.site.register(ExpenseType, ExpenseTypeAdmin)
admin.site.register(Transactions)
admin.site.register(OperationType)


