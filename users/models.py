from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
from newspapers.models import Newspapers
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.core.validators import MaxValueValidator, MinValueValidator


GENDER_CHOICES = (('Others','Others'), ('Male','Male'),('Female','Female'))

# Create your models here.

class Users(models.Model):
	u_name = models.OneToOneField(User,
		verbose_name = "User Name"
		)
	
	mob_no = models.PositiveIntegerField(
		null = False,
		blank = False,
		unique=True,
		)
	

	email_id = models.EmailField(
		null = False,
		blank = False,
		unique=True
		)
	
	joining_date = models.DateTimeField(
		default = timezone.now)

	total_bill=models.FloatField(default=0,)
	
	
	def __str__(self):
		return str(self.u_name)

	class Meta:
		verbose_name = "Users"
		verbose_name_plural = "Users"

class UserInfo(models.Model):
	user_link = models.OneToOneField(
		Users,
		verbose_name = "of user"
		)

	full_name = models.CharField(
		max_length = 250,
		null = True,
		blank = True
		)

	sex = models.CharField(
		max_length = 30,
		choices = GENDER_CHOICES
		)

	address = models.TextField(
		null = True,
		blank = True
		)

	area_code=models.PositiveIntegerField( validators=[MaxValueValidator(999999),MinValueValidator(100001)],default=100001)
		

	profile_pic = models.ImageField(
		upload_to= 'profile_pic',
		null = True,
		blank = True
		)


	class Meta:
		verbose_name = "Users Info"
		verbose_name_plural = "Users Info"

	def __str__(self):
		return self.full_name
			
	