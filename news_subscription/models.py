from __future__ import unicode_literals
from newspapers.models import Newspapers
from django.utils import timezone
from users.models import Users
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Subscription(models.Model):
	sub_paper = models.ManyToManyField(Newspapers, verbose_name= "subscribed for",related_name="papers_subscribed")
	sub_user = models.OneToOneField(Users, verbose_name = "subscriber", related_name="sub_by_user")
	start_date = models.DateField(max_length = 8,default=timezone.now)
	address = models.TextField(blank=False, null=False, default= "default")
	pin_code=models.PositiveIntegerField( validators=[MaxValueValidator(999999),MinValueValidator(100001)],default=100001)


	def __str__(self):
		return str(self.sub_user.u_name)

	class Meta:
		verbose_name = " Subscriptions"
		verbose_name_plural = "Subscriptions"

