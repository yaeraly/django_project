from django.db import models

class Question(models.Model):
    PRIORITY = [
        ('L', 'Low'),
        ('M', 'Medium'),
        ('H', 'High'),
    ]
    title                   = models.CharField(max_length=60)
    question                = models.TextField(max_length=400)
    priority                = models.CharField(max_length=1, choices=PRIORITY)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'The Question'
        verbose_name_plural = 'Peoples questions'
