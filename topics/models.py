from __future__ import unicode_literals
from django.db import models
from genres.models import Genres
# Create your models here.

class Topics(models.Model):
	headline=models.TextField(null=False,blank=False)
	genre=models.ForeignKey('genres.Genres',on_delete=models.CASCADE,related_name='topics')
	class Meta:
		verbose_name = "Topics"
		verbose_name_plural = "Topics"

	def __str__(self):
		return str(self.genre)

