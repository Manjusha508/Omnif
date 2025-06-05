from rest_framework import serializers
from .models import Fitness,Booking
from django.utils.timezone import now

class FitnessSerializer(serializers.ModelSerializer):
    class Meta:
        model=Fitness
        fields = '__all__'
    
class BookingSerializer(serializers.ModelSerializer):
    fitness_name = serializers.CharField(source='fitness_class.name', read_only=True)
    instructor = serializers.CharField(source='fitness_class.instructor', read_only=True)
    fitness_class = serializers.PrimaryKeyRelatedField(
        queryset=Fitness.objects.filter(date_time__gte=now()).order_by('date_time'),
        allow_null=True,
        required=True,
        label="Fitness class"
    )
    class Meta:
        model = Booking
        fields = ['id', 'client_name', 'client_email', 'fitness_class', 'fitness_name', 'instructor']