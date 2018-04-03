from __future__ import unicode_literals

from django.db import models
from users.models import Users
from django.core.validators import MaxValueValidator, MinValueValidator
pin_code=models.PositiveIntegerField( validators=[MaxValueValidator(999999),MinValueValidator(100001)],default=100001)
# Create your models here.

class Vendor(models.Model):
	name = models.CharField(max_length=30,null=False,blank=False)
	vendor_pic = models.ImageField(upload_to = "vendors_pic",)
	VIN = models.IntegerField()
	address = models.TextField(default="address")
	contact_no = models.IntegerField(default="0000000000")
	area_code=models.PositiveIntegerField( validators=[MaxValueValidator(999999),MinValueValidator(100001)],default=100001)
	class Meta:
		verbose_name = "Vendor"
		verbose_name_plural = "Vendors"

	def __str__(self):
		return self.name
	
		
	
		

