from django.db import models
from django.conf import settings

from django.contrib.auth.models import User



class Park(models.Model):
    place = models.CharField(max_length=1)
    time = models.TimeField()



    def __str__(self):
        return self.place

# Create your models here.
