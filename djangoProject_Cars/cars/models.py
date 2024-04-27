from django.db import models

CAR_COMPANY=(
    ('TESLA', 'Tesla'),
    ('BMW', 'BMW'),
    ('MERCEDES', 'Mercedes'),
    ('FORD', 'Ford'),
    ('HONDA', 'Honda'),
)

class Car(models.Model):
    title = models.CharField(max_length=50, unique=True)
    description = models.TextField(
        'description of the car',
        max_length=2000,
        null=True,
        blank=True)
    location = models.CharField(
        max_length=50,
        default='Armenia, Yerevan')
    year=models.PositiveIntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    status=models.BooleanField(default=True)
    image=models.ImageField(
        upload_to='media/car/')
    car_company=models.CharField(
        max_length=10,
        choices=CAR_COMPANY)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Car'
        verbose_name_plural='Cars'


class Service(models.Model):
    car = models.CharField(max_length=20)
    service_center = models.CharField(max_length=20)
    service_date = models.DateField()
    description = models.TextField()


class Custumer(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    phone=models.CharField(max_length=50, unique=True)
    address=models.TextField(max_length=50)
    email=models.EmailField(
        max_length=50,
        unique=True)

class Payment(models.Model):
    card_number=models.CharField(max_length=50, unique=True)
    card_holder_name=models.TextField(max_length=50)
    exp_month=models.PositiveIntegerField()
    exp_year=models.PositiveIntegerField()
    cvv=models.PositiveIntegerField(max_length=3, unique=True)

class Location(models.Model):
    city=models.CharField(max_length=30)
    state=models.CharField(max_length=20)
    country=models.CharField(max_length=20)
    zip=models.CharField(max_length=10)

class Order(models.Model):
    car=models.CharField(max_length=50)
    date=models.DateField()
    delivery_date=models.DateField()
    trucking_number=models.CharField(max_length=50)