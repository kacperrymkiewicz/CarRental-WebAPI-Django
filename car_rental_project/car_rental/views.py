from django.http import HttpResponse
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly, IsAuthenticated
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
    permission_classes = [IsAuthenticated]


class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    name = 'car-detail'
    permission_classes = [IsAuthenticated]


class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    name = 'customer-list'
    permission_classes = [IsAdminUser]
    search_fields = ['name', 'surname', 'email']
    ordering_fields = ['name', 'email']


class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    name = 'customer-detail'
    permission_classes = [IsAdminUser]


class RentalList(generics.ListCreateAPIView):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer
    name = 'rental-list'
    permission_classes = [IsAuthenticated]


class RentalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer
    name = 'rental-detail'
    permission_classes = [IsAuthenticated]


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
    permission_classes = [IsAuthenticated]


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    name = 'review-detail'
    permission_classes = [IsAuthenticated]


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({'cars': reverse(CarList.name, request=request),
                         'customers': reverse(CustomerList.name, request=request),
                         'rentals': reverse(RentalList.name, request=request),
                         'accidents': reverse(AccidentList.name, request=request),
                         'reviews': reverse(ReviewList.name, request=request)
                         })
