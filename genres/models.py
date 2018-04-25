# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Genres(models.Model):
	name=models.CharField(max_length=30,null=False,blank=False)
	genre_img=models.ImageField(upload_to="genres_image",null=True,blank=True)



	class Meta:
		verbose_name = "Genres"
		verbose_name_plural = "Genres"

	def __str__(self):
		return self.name
