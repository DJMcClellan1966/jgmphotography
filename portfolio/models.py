from django.db import models

class Portfolio(models.Model):
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(null=True)

def get_absolute_url(self):
        return reverse('article_detail', kwargs={'slug': self.slug})
