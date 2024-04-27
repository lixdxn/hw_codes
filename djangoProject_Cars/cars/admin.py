from django.contrib import admin

from cars.models import Car, Service, Custumer, Payment, Location, Order

admin.site.register(Car)
admin.site.register(Service)
admin.site.register(Custumer)
admin.site.register(Payment)
admin.site.register(Location)
admin.site.register(Order)