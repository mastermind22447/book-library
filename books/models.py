from django.db import models
from django.contrib.auth.models import User


CHOICES = (
        ('History', 'hi'),
        ('Roman', 'rm'),
    )

class Book(models.Model):
    title = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    author = models.CharField(max_length=200, blank=True, null=True)
    kind = models.CharField(max_length=200, blank=True, null=True, choices=CHOICES,)
    year = models.IntegerField(null=True)
    available = models.BooleanField(default=True )
    

    def __str__(self):
        return str(self.title)


