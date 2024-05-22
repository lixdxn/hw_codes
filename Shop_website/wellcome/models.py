from django.db import models


# Create your models here.
class Home(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=100)
    image = models.ImageField(upload_to='home_images')

    def __str__(self):
        return self.title