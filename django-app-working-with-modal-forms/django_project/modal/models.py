from django.db import models

class Employee(models.Model):
	first_name 	= models.CharField(max_length=30)
	last_name 	= models.CharField(max_length=30)
	full_name 	= models.CharField(max_length=60, blank=True)
	email		= models.EmailField(max_length=30)

	def __str__(self):
		return self.first_name

	def save(self, *args, **kwargs):
		self.full_name = '{0} {1}'.format(self.first_name, self.last_name)
		super(Employee, self).save(*args, **kwargs)