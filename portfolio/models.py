from django.db import models

class Portfolio(models.Model):
    image = models.ImageField(upload_to='images/')
    
