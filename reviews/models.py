from django.db import models

# Create your models here.

class Review(models.Model):
    username = models.CharField(max_length=10)
    review_text = models.CharField(max_length=500)
    rating = models.IntegerField()