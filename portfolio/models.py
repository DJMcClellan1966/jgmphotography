from django.db import models

class Portfolio(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=50, blank=True)
    summary = models.CharField(max_length=250,blank=True)
