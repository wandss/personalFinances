#*-* coding:utf-8 *-*
from django.db import models

class NavMenu(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']


class MainMenu(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    image_name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']
