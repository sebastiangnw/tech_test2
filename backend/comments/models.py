""" This file contains the models """

from datetime import datetime
from django.db import models

# Create your models here.


class Comment(models.Model):
    """This class defines the model for a task."""
    name = models.CharField(max_length=200)
    comment = models.TextField(max_length=5000)
    user = models.CharField(max_length=200)
    created = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name + " - by " + self.user
