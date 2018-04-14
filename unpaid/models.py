from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from newspapers.models import Newspapers
from users.models import Users
# Create your models here.

class Unpaid(models.Model):
	sub_paper = models.ForeignKey(Newspapers, verbose_name= "subscribed for",related_name="unpaid_paper")
	sub_user = models.ForeignKey(Users, verbose_name = "subscriber", related_name="unpaid_subscriber")
	start_date = models.DateField(max_length = 8)
	end_date = models.DateField(max_length=8,default=timezone.now)
	bill=models.FloatField()
	class Meta:
		verbose_name = "Unpaid"
		verbose_name_plural = "Unpaids"

	def __str__(self):
		return str(self.sub_user.email_id)
