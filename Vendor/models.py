from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from users.models import Users
from django.core.validators import MaxValueValidator, MinValueValidator
pin_code=models.PositiveIntegerField( validators=[MaxValueValidator(999999),MinValueValidator(100001)],default=100001)
# Create your models here.

class Vendor(models.Model):

	VIN = models.IntegerField(unique=True)
	username=models.ForeignKey(User,related_name="vendor")
	name = models.CharField(max_length=30,null=False,blank=False)
	email_id=models.EmailField()
	vendor_pic = models.ImageField(upload_to = "vendors_pic",)
	address = models.TextField(default="address")
	contact_no = models.IntegerField(default="0000000000")
	area_code=models.PositiveIntegerField( validators=[MaxValueValidator(999999),MinValueValidator(100001)],default=100001)
	class Meta:
		verbose_name = "Vendor"
		verbose_name_plural = "Vendors"

	def __str__(self):
		return self.name
	
		
	
		

