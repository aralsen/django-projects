from django.db import models


# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=300)
    date_posted = models.DateTimeField(auto_now_add=True)


class Review(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    reviewer = models.CharField(max_length=200)
    reviewer_title = models.CharField(max_length=85)
