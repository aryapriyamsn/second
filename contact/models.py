from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Contact(models.Model):
	recipent=models.CharField(max_length=40,null=True,blank=True)
	email=models.EmailField(null=False,blank=False,unique=True)
	message=models.TextField(null=False,blank=False)

	class Meta:
		verbose_name = "Contact"
		verbose_name_plural = "Contact"

	def __str__(self):
		return self.recipent
	
class Newsletter(models.Model):
	
	email=models.EmailField(null=False,blank=False,unique=True)
	
	class Meta:
		verbose_name = "Newsletter"
		verbose_name_plural = "Newsletters"

	def __str__(self):
		return self.email

class Work(models.Model):
	requester=models.CharField(max_length=40,null=True,blank=True)
	email=models.EmailField(null=False,blank=False,unique=True)
	message=models.TextField(null=False,blank=False)

	class Meta:
		verbose_name = "Work"
		verbose_name_plural = "Work"

	def __str__(self):
		return self.requester