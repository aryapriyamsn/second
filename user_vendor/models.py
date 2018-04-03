from __future__ import unicode_literals

from django.db import models
from users.models import Users
from Vendor.models import Vendor
# Create your models here.

class Customers(models.Model):
	customer = models.ManyToManyField(Users, verbose_name='customer', related_name='vendor_is')
	vendor = models.ManyToManyField(Vendor, verbose_name='vendor', related_name='of_customer')

	class Meta:
		verbose_name = "Customer"
		verbose_name_plural = "Customers"

	def __str__(self):
		return str(self.customer.all()[0])
	