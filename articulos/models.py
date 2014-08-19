from django.db import models

class Seccion(models.Model):
	codigo = models.CharField(max_length=15, primary_key=True)
	nombre = models.CharField(max_length=60)

class Articulo(models.Model):
	codigo = models.CharField(max_length=15, primary_key=True)
	nombre = models.CharField(max_length=60)
	info_adicional = models.TextField(max_length=250)


