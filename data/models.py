from django.db import models

class TSG(models.Model):
    centro = models.CharField(max_length=7)
    ano = models.IntegerField(default=0)
    codcurso = models.IntegerField(default=0)
    nomecurso = models.CharField(max_length=50)
    ingressantes = models.IntegerField(default=0)
    formados = models.IntegerField(default=0)
    matriculados = models.IntegerField(default=0)
    tsgtaxa = models.FloatField(default=0)
    tsgcentro = models.FloatField(default=0)
    tsgufsm = models.FloatField(default=0)
    anoingresso = models.IntegerField(default=0)
    def __unicode__(self):
        return self.centro