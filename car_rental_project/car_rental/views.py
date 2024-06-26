from django.http import HttpResponse
from django_filters import FilterSet, DateTimeFilter, NumberFilter, AllValuesFilter
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Car, Customer, Rental, Accident, Review
from .serializers import CarSerializer, CustomerSerializer, RentalSerializer, AccidentSerializer, ReviewSerializer
from .permissions import IsOwnerOrReadOnly


def index(request):
    return HttpResponse("Hello, world.")


class CarFilter(FilterSet):
    min_price = NumberFilter(field_name='price', lookup_expr='gte')
    max_price = NumberFilter(field_name='price', lookup_expr='lte')
    client_name = AllValuesFilter(field_name='client__surnamename')

    class Meta:
        model = Car
        fields = ['min_price', 'max_price', 'client_name']


class CarList(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    name = 'car-list'
    permission_classes = [IsAuthenticated]
    filter_class = CarFilter


class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    name = 'car-detail'
    permission_classes = [IsAuthenticated]


class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    name = 'customer-list'
    permission_classes = [IsAuthenticated]
    search_fields = ['name', 'surname', 'email']
    ordering_fields = ['name', 'email']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    name = 'customer-detail'
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


class RentalFilter(FilterSet):
    from_pickup_date = DateTimeFilter(field_name='pickup_date', lookup_expr='gte')
    to_pickup_date = DateTimeFilter(field_name='pickup_date', lookup_expr='lte')
    from_return_date = DateTimeFilter(field_name='return_date', lookup_expr='gte')
    to_return_date = DateTimeFilter(field_name='return_date', lookup_expr='lte')

    class Meta:
        model = Rental
        fields = ['from_pickup_date', 'to_pickup_date', 'from_return_date', 'to_return_date']


class RentalList(generics.ListCreateAPIView):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer
    name = 'rental-list'
    permission_classes = [IsAuthenticated]
    filter_class = RentalFilter
    ordering_fields = ['pickup_date', 'return_date']


class RentalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer
    name = 'rental-detail'
    permission_classes = [IsAuthenticated]


class AccidentList(generics.ListCreateAPIView):
    queryset = Accident.objects.all()
    serializer_class = AccidentSerializer
    name = 'accident-list'
    permission_classes = [IsAuthenticated]


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

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    name = 'review-detail'
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({'cars': reverse(CarList.name, request=request),
                         'customers': reverse(CustomerList.name, request=request),
                         'rentals': reverse(RentalList.name, request=request),
                         'accidents': reverse(AccidentList.name, request=request),
                         'reviews': reverse(ReviewList.name, request=request)
                         })
