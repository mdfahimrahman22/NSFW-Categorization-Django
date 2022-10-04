from django.db import models

# Create your models here.
class RowTrack(models.Model):
    current_index = models.IntegerField(default=0)
    pornography_count=models.IntegerField(default=0)
    misogyny_count=models.IntegerField(default=0)
    malignant_stereotypes_count=models.IntegerField(default=0)
    malign_count=models.IntegerField(default=0)
    delete_count=models.IntegerField(default=0)