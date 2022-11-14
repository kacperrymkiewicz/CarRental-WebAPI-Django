from django.http import HttpResponse
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Car, Customer, Rental, Accident, Review
from .serializers import CarSerializer, CustomerSerializer, RentalSerializer, AccidentSerializer, ReviewSerializer


def index(request):
    return HttpResponse("Hello, world.")


class CarList(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    name = 'car-list'


class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    name = 'car-detail'


class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    name = 'customer-list'


class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    name = 'customer-detail'


class RentalList(generics.ListCreateAPIView):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer
    name = 'rental-list'


class RentalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer
    name = 'rental-detail'


class AccidentList(generics.ListCreateAPIView):
    queryset = Accident.objects.all()
    serializer_class = AccidentSerializer
    name = 'accident-list'
    permission_classes = [IsAdminUser]


class AccidentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Accident.objects.all()
    serializer_class = AccidentSerializer
    name = 'accident-detail'
    permission_classes = [IsAdminUser]


class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    name = 'review-list'


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    name = 'review-detail'


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({'cars': reverse(CarList.name, request=request),
                         'customers': reverse(CustomerList.name, request=request),
                         'rentals': reverse(RentalList.name, request=request),
                         'accidents': reverse(AccidentList.name, request=request),
                         'reviews': reverse(ReviewList.name, request=request)
                         })
