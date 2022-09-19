from django.db import models

# Create your models here.
class RowTrack(models.Model):
    current_index = models.IntegerField(default=0)