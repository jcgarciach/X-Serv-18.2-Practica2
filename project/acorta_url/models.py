
from django.db import models

# Create your models here.

class urls (models.Model):
    url_large = models.CharField(max_length = 64)
