from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),
    path('cars', views.CarList.as_view(), name=views.CarList.name),
    path('cars/<int:pk>', views.CarDetail.as_view(), name=views.CarDetail.name),
    path('customers', views.CustomerList.as_view(), name=views.CustomerList.name),
    path('customers/<int:pk>', views.CustomerDetail.as_view(), name=views.CustomerDetail.name),
    path('rentals', views.RentalList.as_view(), name=views.RentalList.name),
    path('rentals/<int:pk>', views.RentalDetail.as_view(), name=views.RentalDetail.name),
    path('accidents', views.AccidentList.as_view(), name=views.AccidentList.name),
    path('accidents/<int:pk>', views.AccidentDetail.as_view(), name=views.AccidentDetail.name),
    path('reviews', views.ReviewList.as_view(), name=views.ReviewList.name),
    path('reviews/<int:pk>', views.ReviewDetail.as_view(), name=views.RentalDetail.name)
]
