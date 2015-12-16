from django.db import models

# Create your models here.
class CPC(models.Model):
	AREA = models.CharField(max_length=20)
	UF = models.CharField(max_length=2)
	REGIAO = models.IntegerField(default=0)
	ANO = models.IntegerField(default=0)
	CPCCONTINUO	= models.FloatField(default=0)
	NOTACONCLUINTES	= models.FloatField(default=0)
	NOTAPADRONIZADAIDD	= models.FloatField(default=0)
	NOTAPADRONIZADAMESTRES = models.FloatField(default=0)
	NOTAPADRONIZADADOUTORES = models.FloatField(default=0)
	NOMEIES	 = models.CharField(max_length=50)
	SIGLAIES = models.CharField(max_length=15)
	PUB_PRIV = models.IntegerField(default=0)
	ORGACADEMICA = models.CharField(max_length=20)
	MUNICIPIOCURSO = models.CharField(max_length=50)
	NOTAPADRONIZADADREGIME = models.FloatField(default=0)
	NOTAPADRONIZADAPEDAG = models.FloatField(default=0)
	CPC_FAIXA = models.FloatField(default=0)
	NOTAPADRONIZADAINFRA = models.FloatField(default=0)
	INGRESSANTESPARTICIPANTES = models.IntegerField(default=0)
	INGRESSANTESINSCRITOS = models.IntegerField(default=0)
	COD_AREA = models.IntegerField(default=0)
	COD_IES	= models.IntegerField(default=0)
	AMPLIACAOFORMACAO_NA = models.FloatField(default=0)
	CPC_FORMULA2013 = models.FloatField(default=0)
	def __unicode__(self):
		return self.AREA + " " + self.SIGLAIES


class TSG(models.Model):
	CENTRO = models.CharField(max_length=50)
	ANO	= models.IntegerField(default=0)
	CODCURSO = models.IntegerField(default=0)
	NOMECURSO = models.CharField(max_length=50)
	INGRESSANTES = models.IntegerField(default=0)
	FORMADOS = models.IntegerField(default=0)
	MATRICULADOS = models.IntegerField(default=0)
	TSGTAXA	= models.FloatField(default=0)
	TSGCENTRO = models.FloatField(default=0)
	TSGUFSM	= models.FloatField(default=0)
	ANOINGRESSO = models.IntegerField(default=0)
	def __unicode__(self):
		return self.NOMECURSO
