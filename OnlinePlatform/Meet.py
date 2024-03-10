
from django.db import models

class Link(models.Model):
    meeting_name = models.CharField(max_length=500)
    meeting_link = models.URLField(max_length=2000)
    start = models.TimeField(default='12:00:00')
    end = models.TimeField(default='12:00:00')
    mon = models.BooleanField(default=False)
    tue = models.BooleanField(default=False)
    wed = models.BooleanField(default=False)
    thus = models.BooleanField(default=False)
    fri = models.BooleanField(default=False)
    sat = models.BooleanField(default=False)










