from django.contrib import admin
from .models import Car, Customer, Rental, Accident, Review

# Register your models here.
admin.site.register(Car)
admin.site.register(Customer)
admin.site.register(Rental)
admin.site.register(Accident)
admin.site.register(Review)
