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
    owner = models.ForeignKey('auth.User', related_name='customers', on_delete=models.CASCADE)

    def __str__(self):
        return self.firstname + " " + self.lastname


class Rental(models.Model):
    pickup_date = models.DateField()
    return_date = models.DateField()
    customer = models.ForeignKey(Customer, related_name='rentals', on_delete=models.CASCADE)
    car = models.ForeignKey(Car, related_name='rentals', on_delete=models.CASCADE)
    status = models.BooleanField()

    def __str__(self):
        return "From " + str(self.pickup_date) + " to " + str(self.return_date) + ": " + self.customer.lastname + " - " + self.car.brand + " " + self.car.model


class Accident(models.Model):
    COLLISION = 'C'
    BREAKDOWN = 'B'
    OTHER = 'O'
    TYPES = ((COLLISION, 'Car collision'), (BREAKDOWN, 'Car breakdown'), (OTHER, 'Other accident'))
    type = models.CharField(max_length=2, choices=TYPES, default=COLLISION)
    description = models.CharField(max_length=500)
    rental = models.ForeignKey(Rental, related_name='accidents', on_delete=models.CASCADE)

    def __str__(self):
        return "Accident: " + self.type + ", " + self.rental.car.brand + " " + self.rental.car.model + " - " + self.rental.customer.lastname


class Review(models.Model):
    stars = models.IntegerField()
    date = models.DateField()
    customer = models.ForeignKey(Customer, related_name='reviews', on_delete=models.CASCADE)
    car = models.ForeignKey(Car, related_name='reviews', on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User', related_name='reviews', on_delete=models.CASCADE)

    def __str__(self):
        return "Review: " + str(self.stars) + " stars, " + self.customer.lastname + ", " + self.car.brand + " " + self.car.model
