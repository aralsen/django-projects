from django.db import models


# Create your models here.

class Coin(models.Model):
    name = models.CharField(max_length=100)
    photo_url = models.URLField()

    def __str__(self):
        return self.name
