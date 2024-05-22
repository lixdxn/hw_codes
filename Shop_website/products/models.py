from django.db import models

# Create your models here.
class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Product(TimeStampedModel):
    photo = models.ImageField(upload_to='images')
    name = models.CharField(max_length=20)
    price = models.FloatField(default=0)
    slug = models.SlugField(unique=True)
    description = models.TextField(max_length=100)

    def __str__(self):
        return self.name