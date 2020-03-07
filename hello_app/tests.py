from django.test import TestCase, Client
from django.db.models import Max

from .models import AirPort, Flight, Passenger
# Create your tests here.

class ModelsTestCase(TestCase):
	#setting up testing enviroments
	def setUp(self):
		#create airports
		a1 = AirPort.objects.create(code='AAA', city ='City A')
		a2 = AirPort.objects.create(code='BBB', city ='City B')

		#create flights which will be tested if it's crated correctly
		Flight.objects.create(origin = a1, destination = a2, duration = 100)
		Flight.objects.create(origin = a1, destination = a1, duration = 200)
		Flight.objects.create(origin = a1, destination = a2, duration = -100)

	def test_departures_count(self):
		#instanting the airport which code is AAA
		a = AirPort.objects.get(code='AAA')
		#testing if amount of departures equals 3
		self.assertEqual(a.departures.count(), 3)


	def test_arrivals_count(self):
		a = AirPort.objects.get(code='AAA')
		self.assertEqual(a.arrivals.count(), 1)

	def test_valid_flights(self):
		a1 = AirPort.objects.get(code='AAA')
		a2 = AirPort.objects.get(code='BBB')
		f = Flight.objects.get(origin = a1, destination=a2, duration=100)
		self.assertTrue(f.is_valid_flight())

	def test_invalid_fligtht_destination(self):
		a1 = AirPort.objects.get(code='AAA')
		f = Flight.objects.get(origin = a1, destination = a1)
		self.assertFalse(f.is_valid_flight())

	def test_invalid_fligtht_duration(self):
		a1 = AirPort.objects.get(code='AAA')
		a2 = AirPort.objects.get(code='BBB')
		f = Flight.objects.get(origin = a1, destination = a2, duration=-100)
		self.assertFalse(f.is_valid_flight())

	def test_index(self):
		c = Client()
		response = c.get('/')
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.context["flights"].count(), 3)

	def test_valid_frena(self):
		a1 = AirPort.objects.get(code ='AAA')
		f = Flight.objects.get(origin = a1, destination=a1)
		c = Client()
		response = c.get(f"/{f.id}")
		self.assertEqual(response.status_code, 200)

	def test_invalid_frena(self):
		max_id = Flight.objects.all().aggregate(Max('id'))["id__max"]
		c = Client()
		response = c.get(f"/{max_id + 1}")
		self.assertEqual(response.status_code,404)

	def test_frena_page_tvt_mgzavrebi(self):
		f = Flight.objects.get(pk=1)
		p = Passenger.objects.create(first_name='Amiran', last_name='Kalandia')
		f.passengers.add(p)

		c= Client()
		response = c.get(f"/{f.id}")
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.context["tvt_mgzavrebi"].count(), 1)

	def test_frena_page_non_passengers(self):
		f = Flight.objects.get(pk=1)
		p = Passenger.objects.create(first_name='Amiran', last_name='Kalandia')

		c = Client()
		response = c.get(f"/{f.id}")
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.context["non_passengers"].count(), 1)








		


