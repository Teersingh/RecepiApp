from django.db import models

# Create your models here.


class recepies(models.Model):

    recepi_n = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='Image/')

    