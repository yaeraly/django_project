from django.db import models

class Person(models.Model):
	first_name		= models.CharField(max_length=50)
	last_name 		= models.CharField(max_length=50)
	full_name		= models.CharField(max_length=101, blank=True)

	def __str__(self):
		return self.first_name


	def save(self, *args, **kwargs):
		self.full_name = self.first_name + ' ' + self.last_name

		super(Person, self).save(*args, **kwargs)
