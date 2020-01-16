from django.db import models

from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=50)
    pub_date = models.DateField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def summary(self):
        return self.body[:100]

    def __str__(self):
        return self.title

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')    
