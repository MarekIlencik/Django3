from django.db import models

# Create your models here.
class Projekty(models.Model):
    image = models.ImageField(upload_to = 'images/')
    popis = models.CharField(max_length = 200)
