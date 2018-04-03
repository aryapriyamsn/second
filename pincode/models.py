from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Pincode(models.Model):
	pin=models.IntegerField()

	class Meta:
		verbose_name = "Pincode"
		verbose_name_plural = "Pincode"

	def __str__(self):
		return str(self.pin)

class Available(models.Model):
	pincode = models.IntegerField()
	class Meta:
		verbose_name = "Available"
		verbose_name_plural = "Available"

	def __str__(self):
		return str(self.pincode)
	