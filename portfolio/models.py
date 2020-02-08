from django.db import models
from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class Portfolio(models.Model):
    image = models.ImageField(upload_to='images/')
    photographer_name = models.CharField(max_length=100, blank = True)
    title = models.CharField(max_length=100, blank = True)

    def __str__(self):
        return (self.title)
