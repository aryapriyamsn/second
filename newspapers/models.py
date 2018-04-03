from __future__ import unicode_literals
from multiselectfield import MultiSelectField

from django.db import models

LANG_CHOICES = (('English','English'), ('Hindi','Hindi'), ('Marathi','Marathi'), ('Kannada','Kannada'), ('Tamil','Tamil'),('Telugu','Telugu'),('Urdu','Urdu'),('Bengali','Bengali'))
DAYS_CHOICES = (('All Days','All Days'), ('Weekends','Weekends'), ('Weekdays','Weekdays'), ('Monday','Monday'), ('Tuesday','Tuesday'),('Wednesday','Wednesday'),('Thursday','Thursday'),('Friday','Friday'),('Saturday','Saturday'),('Sunday','Sunday'))
AREAS = (('Powai','Powai'),('Ghansoli','Ghansoli'))
TIMING = (('Morning','Morning'),('Evening','Evening'))
# Create your models here.


class Newspapers(models.Model):
	title = models.CharField(
		max_length = 30,
		null = False,
		blank = False,
		)

	language = MultiSelectField(
		choices = LANG_CHOICES,
		null = False,
		blank = False,
		)
	price = models.DecimalField(
		max_digits = 10,
		decimal_places= 2,
		)
	
	days = MultiSelectField(
		choices = DAYS_CHOICES,
		null = True,
		blank = True,
		)

	area = MultiSelectField(
		choices = AREAS,
		null = True,
		blank = True,
		)

	timing = models.CharField(
		max_length = 20,
		choices = TIMING,
		null = True,
		blank = True,)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = "Newspapers"
		verbose_name_plural = "Newspapers"




