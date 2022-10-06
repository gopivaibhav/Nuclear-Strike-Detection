from django.db import models
from datetime import datetime

# Create your models here.
class Tweets(models.Model):
    striked = models.FloatField()
    time = models.DateTimeField(default = datetime.now)

    def __str__(self):
        return str(self.time)