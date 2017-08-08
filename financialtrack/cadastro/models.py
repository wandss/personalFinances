#-*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from .choices import tipo_choices



class TipoDespesa(models.Model):
    nome = models.CharField(max_length=100)
    data_inclusao = models.DateTimeField(default=timezone.now)
    incluido_por = models.ForeignKey('auth.User')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Tipos de Depesas'
        ordering = ['nome']
        unique_together = ('nome','incluido_por')


class Transacoes(models.Model):
    estabelecimento = models.CharField(max_length=100)
    despesa = models.ForeignKey(TipoDespesa,on_delete=models.PROTECT)
    tipo_trans = models.IntegerField(choices=tipo_choices)
    data = models.DateTimeField(default=timezone.now)
    valor = models.DecimalField(max_digits=9, decimal_places=2)
    informacoes = models.CharField(max_length=100, null=True, blank=True)
    incluido_por = models.ForeignKey('auth.User')
    repeat = models.BooleanField(default=False)
    total_repeats = models.IntegerField(default=0)


    def __str__(self):
        return self.estabelecimento

    class Meta:
        verbose_name_plural = "Transações"
        ordering = ['-data']
