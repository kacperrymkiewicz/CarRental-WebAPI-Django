from rest_framework import serializers
from .models import Car, Customer, Rental, Accident, Review


class CarSerializer(serializers.HyperlinkedModelSerializer):
    rentals = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='rental-detail')
    reviews = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='review-detail')

    class Meta:
        model = Car
        fields = ['id', 'url', 'brand', 'model', 'type', 'production_year', 'price', 'registration_plate', 'rentals', 'reviews']


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    rentals = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='rental-detail')
    reviews = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='review-detail')
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Customer
        fields = ['id', 'url', 'firstname', 'lastname', 'phone_number', 'zip_code', 'city', 'street', 'house_number', 'owner', 'rentals', 'reviews']

    def validate_firstname(self, value):
        if value.capitalize() != value:
            raise serializers.ValidationError("First name should start with a capital letter.")
        return value

    def validate_lastname(self, value):
        if value.capitalize() != value:
            raise serializers.ValidationError("Last name should start with a capital letter.")
        return value

    def validate_city(self, value):
        if value.capitalize() != value:
            raise serializers.ValidationError("City should start with a capital letter.")
        return value


class RentalSerializer(serializers.HyperlinkedModelSerializer):
    accidents = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='accident-detail')
    customer = serializers.SlugRelatedField(queryset=Customer.objects.all(), slug_field='lastname')
    car = serializers.SlugRelatedField(queryset=Car.objects.all(), slug_field='model')

    class Meta:
        model = Rental
        fields = ['id', 'url', 'pickup_date', 'return_date', 'customer', 'car', 'status', 'accidents']


class AccidentSerializer(serializers.HyperlinkedModelSerializer):
    type = serializers.ChoiceField(choices=Accident.TYPES)
    rental = serializers.StringRelatedField()

    class Meta:
        model = Accident
        fields = ['id', 'url', 'type', 'description', 'rental']


class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    customer = serializers.SlugRelatedField(queryset=Customer.objects.all(), slug_field='lastname')
    car = serializers.SlugRelatedField(queryset=Car.objects.all(), slug_field='model')

    class Meta:
        model = Review
        fields = ['id', 'url', 'stars', 'date', 'customer', 'car']

    def validate_stars(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("The number of stars should be between 1 and 5.")
        return value
