from django.db import models

CAR_COLOR = (
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('red', 'Red'),
    ('yellow', 'Yellow'),
    ('black', 'Black'),
)

STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published'),
)

# Create your models here.
class Manufacture(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, default='', blank=True)
    address = models.TextField()
    photo = models.ImageField(upload_to='photos/')
    draft = models.BooleanField(default=False)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return self.name

class Car(models.Model):
    manufacture = models.ForeignKey(Manufacture, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    date = models.DateField()
    car_color = models.CharField(max_length=20, choices=CAR_COLOR)
    photo = models.ImageField(upload_to='photos/')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)