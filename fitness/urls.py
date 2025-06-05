from django.urls import path 
from .views import Fitnessview,Bookview,Bookingbyemail,BookingDeleteView,FitnessCreateView,FitnessDeleteView

urlpatterns=[
    path('classes/',Fitnessview.as_view()),
    path('classes/create/', FitnessCreateView.as_view(), name='fitness-create'),
    path('book/',Bookview.as_view()),
    path('bookings/',Bookingbyemail.as_view()),
    path('booking/delete/<int:id>/', BookingDeleteView.as_view(), name='booking-delete'),
    path('classes/<int:id>/', FitnessDeleteView.as_view(), name='delete_fitness_class'),

]
