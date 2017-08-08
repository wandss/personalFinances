from django.contrib import admin
from cadastro.models import TipoDespesa, Transacoes

class TipoDespesaAdmin(admin.ModelAdmin):

    list_display = ['nome', 'data_inclusao', 'incluido_por']

class TransacoesAdmin(admin.ModelAdmin):

    list_display = ['estabelecimento','despesa', 'tipo_trans', 'data', 'valor','informacoes','repeat','total_repeats']


admin.site.register(TipoDespesa, TipoDespesaAdmin)
admin.site.register(Transacoes, TransacoesAdmin)
