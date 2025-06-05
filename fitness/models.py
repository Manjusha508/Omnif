from django.db import models

# Create your models here.
class Fitness(models.Model):
    name=models.CharField(max_length=100)
    instructor=models.CharField(max_length=100)
    date_time=models.DateField()
    available_slots=models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name}-{self.date_time}"

class Booking(models.Model):
    fitness_class=models.ForeignKey(Fitness,on_delete=models.CASCADE)
    client_name=models.CharField(max_length=100)
    client_email=models.EmailField()

    def __str__(self):
        return f"{self.client_name}-{self.fitness_class.name}"