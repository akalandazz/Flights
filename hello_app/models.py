from django.db import models

# Create your models here.
class AirPort(models.Model):
	code = models.CharField(max_length=3)
	city = models.CharField(max_length = 50)

	def __str__(self):
		return f"{self.city} - {self.code}"


class Flight(models.Model):
	origin = models.ForeignKey(AirPort,on_delete=models.CASCADE, related_name = "departures")#tels if i delete airpot class it automatically deletes flights
	destination = models.ForeignKey(AirPort, on_delete = models.CASCADE, related_name='arrivals')
	duration = models.IntegerField()

	#flight is valid when origin and destionation doesn't equal each other also duration mus be greater then 0
	def is_valid_flight(self):
		return (self.origin != self.destination) and (self.duration >= 0)


	def __str__(self):
		return f"{self.id}-{self.origin} to {self.destination}"


class Passenger(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	reisi = models.ManyToManyField(Flight, blank=True, related_name="passengers")

	def __str__(self):
		return f"{self.first_name}-{self.last_name}"

