from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class StoreFile(models.Model):
    name = models.CharField(max_length=255,blank=True,null=True)
    file = models.FileField(upload_to="files/")
