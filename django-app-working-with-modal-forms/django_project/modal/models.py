from django.db import models

class Post(models.Model):
	title = models.CharField(max_length=30, null=True, blank=True)

	def __str__(self):
		return self.title


class Comment(models.Model):
	content = models.CharField(max_length=300, null=True, blank=True)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)

	def __str__(self):
		return self.content