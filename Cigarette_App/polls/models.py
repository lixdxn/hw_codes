from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Cigarette(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    model = models.CharField(max_length=30)
    description = models.TextField(max_length=100, null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    photo = models.ImageField(upload_to='photos/')


    def __str__(self):
        return self.model
