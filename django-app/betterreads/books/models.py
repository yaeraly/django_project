from django.db import models

class Book(models.Model):
	title 		= models.CharField(max_length=255)
	subtitle 	= models.CharField(max_length=255, blank=True)
	blurb		= models.TextField(blank=True)
	num_pages 	= models.IntegerField(blank=True)
	price		= models.FloatField(blank=True)
	in_print	= models.BooleanField(default=True)

	def __str__(self):
		return self.title

