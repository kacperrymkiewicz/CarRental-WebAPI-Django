from rest_framework import serializers
from .models import Car, Customer, Rental, Accident, Review


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'brand', 'model', 'type', 'production_year', 'price', 'registration_plate']


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'surname', 'email', 'password', 'phone', 'address']

    def validate_name(self, value):
        if value.capitalize() != value:
            raise serializers.ValidationError("First name should start with a capital letter.")
        return value


class RentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rental
        fields = ['id', 'pickup_date', 'return_date', 'customer', 'car', 'status']


class AccidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accident
        fields = ['id', 'type', 'description', 'rental']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['stars', 'date', 'customer', 'car']

    def validate_stars(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("The number of stars should be between 1 and 5.")
        return value
