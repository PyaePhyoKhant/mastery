from django.db import models
from django.contrib.auth.models import User


class Learner(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    points = models.IntegerField()

    def __str__(self):
        return self.name
