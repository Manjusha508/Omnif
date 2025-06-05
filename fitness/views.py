from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response  
from .models import Fitness,Booking
from .serializers import FitnessSerializer,BookingSerializer
from django.utils.timezone import now
from datetime import datetime

# Create your views here.

#GET

class Fitnessview(generics.ListAPIView):
    serializer_class=FitnessSerializer
    
    def get_queryset(self):
        return Fitness.objects.filter(date_time__gte=now()).order_by('date_time')


class FitnessCreateView(generics.CreateAPIView):
    queryset = Fitness.objects.all()
    serializer_class = FitnessSerializer
    
#POST

class Bookview(generics.CreateAPIView):
    serializer_class = BookingSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        fitness_class = serializer.validated_data['fitness_class']
        client_name = serializer.validated_data['client_name']
        client_email = serializer.validated_data['client_email']

         # Validate fitness_class_id and get Fitness object
        
        if fitness_class.available_slots <= 0:
            return Response({"error": "No available slots"}, status=status.HTTP_400_BAD_REQUEST)
        if Booking.objects.filter(client_email=client_email, fitness_class=fitness_class).exists():
            return Response({"error": "You have already booked this class."}, status=status.HTTP_400_BAD_REQUEST)

    
        booking = Booking.objects.create(
            fitness_class=fitness_class,
            client_name=client_name,
            client_email=client_email
        )

        fitness_class.available_slots -= 1
        fitness_class.save()
        output_serializer = self.get_serializer(booking)

        return Response(output_serializer.data, status=status.HTTP_201_CREATED)
#Get/bookings

class Bookingbyemail(generics.ListAPIView):
    serializer_class=BookingSerializer

    def get_queryset(self):
        email=self.request.query_params.get('email')
        if email:
            return Booking.objects.filter(client_email=email)
        return Booking.objects.all()
    
class BookingDeleteView(generics.DestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    lookup_field = 'id'
    def destroy(self, request, *args, **kwargs):
        booking_id = kwargs.get('id')
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {"message": f"Booking id:{booking_id} deleted successfully."},
            status=status.HTTP_200_OK
    )

class FitnessDeleteView(generics.DestroyAPIView):
    queryset = Fitness.objects.all()
    serializer_class = FitnessSerializer
    lookup_field = 'id'
    def destroy(self, request, *args, **kwargs):
        class_id = kwargs.get('id')
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {"message": f"Class id:{class_id} deleted successfully."},
            status=status.HTTP_200_OK
    )