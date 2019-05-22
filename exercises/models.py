from django.db import models

# Create your models here.

class Exercises(models.Model):
    name = models.CharField(max_length = 200)
    weight = models.IntegerField(default = 5)
    sets = models.IntegerField(default = 1)
    reps = models.IntegerField(default = 1)
    def __str__(self):
        return self.name
