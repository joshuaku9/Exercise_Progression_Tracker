from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Exercises(models.Model):
    name = models.CharField(max_length = 200)
    weight = models.IntegerField(default = 5)
    sets = models.IntegerField(default = 1)
    reps = models.IntegerField(default = 1)
    date_created = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete='CASCADE')
    def __str__(self):
        return self.name
