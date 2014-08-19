from django.db import models

class Tercero(models.Model):
	nit_cc = models.CharField(max_length=15)
	dv = models.CharField(max_length=1)
	nombre_o_razon_social = models.CharField(max_length=60)
	nombres = models.CharField(max_length=30)
	apellidos = models.CharField(max_length=30)
	direccion = models.CharField(max_length=60)
	telefono = models.CharField(max_length=60)
	email = models.EmailField(blank=True)
	website = models.URLField(blank=True)

	def __str__(self):
		return self.nombre_o_razon_social

class Contacto(models.Model):
	nombres = models.CharField(max_length=60)
	cargo = models.CharField(max_length=30)
	tercero = models.ForeignKey(Tercero)

	def __str__(self):
		return self.nombres

