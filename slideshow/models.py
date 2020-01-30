from django.db import models
from django.contrib.auth.models import User

class Saved(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    comments = models.TextField(max_length = 250)
