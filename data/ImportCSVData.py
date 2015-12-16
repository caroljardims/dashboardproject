from django.test import TestCase
from model import CsvModel, CsvDbModel, ImproperlyConfigured, CsvException, CsvDataException, TabularLayout, SkipRow
from myTestModel.models import *


class TestCsvModel(CsvModel):
	CURSO = CharField(max_length=20)
	UF = CharField(max_length=2)
	REGIAO = IntegerField(1)
	ANO = IntegerField(4)
	CPCCONTINUO	= FloatField(null=True, blank=True, default=None)
	NOTACONCLUINTES	= FloatField(null=True, blank=True, default=None)
	NOTAPADRONIZADAIDD	= FloatField(null=True, blank=True, default=None)
	NOTAPADRONIZADAMESTRES = FloatField(null=True, blank=True, default=None)
	NOTAPADRONIZADADOUTORES = FloatField(null=True, blank=True, default=None)
	NOMEIES	 = CharField(max_length=50)
	SIGLAIES = CharField(max_length=15)
	Publica_1_Privada_0	= IntegerField(1)
	CATADMINISTRATIVA = CharField(max_length=10)
	ORGACADEMICA = CharField(max_length=20)
	MUNICIPIOCURSO = CharField(max_length=50)
	NOTAPADRONIZADADREGIME = FloatField(null=True, blank=True, default=None)
	NOTAPADRONIZADAPEDAG = FloatField(null=True, blank=True, default=None)
	CPC_FAIXA = FloatField(null=True, blank=True, default=None)
	NOTAPADRONIZADAINFRA = FloatField(null=True, blank=True, default=None)
	INGRESSANTESPARTICIPANTES = IntegerField(5)
	INGRESSANTESINSCRITOS = IntegerField(5)
	COD_CURSO = IntegerField(5)
	COD_IES	= IntegerField(5)
	AMPLIACAOFORMACAO_NA = FloatField(null=True, blank=True, default=None)
	CPC_FORMULA2013 = FloatField(null=True, blank=True, default=None)

	class Meta:
	    delimiter = ","
	    dbModel = CPC

	test_data = ["Roger", "10", "1.8"]