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
    name = models.CharField(max_length=45)
    surname = models.CharField(max_length=45)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    phone = models.CharField(max_length=9)
    address = models.CharField(max_length=120)

    def __str__(self):
        return self.name + " " + self.surname


class Rental(models.Model):
    pickup_date = models.DateField()
    return_date = models.DateField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    status = models.BooleanField()


class Accident(models.Model):
    type = models.CharField(max_length=45)
    description = models.CharField(max_length=500)
    rental = models.ForeignKey(Rental, on_delete=models.CASCADE)


class Review(models.Model):
    stars = models.IntegerField()
    date = models.DateField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)