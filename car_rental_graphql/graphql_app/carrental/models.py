from django.db import models

class Car(models.Model):
    brand = models.CharField(max_length=45)
    model = models.CharField(max_length=100)
    type = models.CharField(max_length=45)
    production_year = models.IntegerField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    registration_plate = models.CharField(max_length=20)

    def __str__(self):
        return self.brand + " " + self.model


class Customer(models.Model):
    firstname = models.CharField(max_length=45)
    lastname = models.CharField(max_length=45)
    phone_number = models.CharField(max_length=9)
    zip_code = models.CharField(max_length=6)
    city = models.CharField(max_length=45)
    street = models.CharField(max_length=45)
    house_number = models.CharField(max_length=5)

    def __str__(self):
        return self.firstname + " " + self.lastname


class Rental(models.Model):
    pickup_date = models.DateField()
    return_date = models.DateField()
    customer = models.ForeignKey(Customer, related_name='rentals', on_delete=models.CASCADE)
    car = models.ForeignKey(Car, related_name='rentals', on_delete=models.CASCADE)

    def __str__(self):
        return "From " + str(self.pickup_date) + " to " + str(self.return_date) + ": " + self.customer.lastname + " - " + self.car.brand + " " + self.car.model