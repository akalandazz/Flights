from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect,Http404
from .models import Flight, Passenger
from django.urls import reverse

# Create your views here.
def index(request):
	context={
		"flights":Flight.objects.all()
	}
	return render(request,"frenebi/index.html", context)


def frena(request, flight_id):
	try:
		frena_ =Flight.objects.get(pk = flight_id)
		#pk - primary key
	except Flight.DoesNotExist:
		raise Http404('Flight does not exist')

	context = {"frena": frena_, "non_passengers":frena_.passengers.all(),
	#this line of code shows us the passengers who aren't registered on particular flight yet
	"tvt_mgzavrebi": Passenger.objects.exclude(reisi=frena_).all()
	}
	return render(request, 'frenebi/frena.html', context)


def book(request, flight_id):
	try:
		passenger_id = int(request.POST["passenger"])
		passenger = Passenger.objects.get(pk=passenger_id)
		flight = Flight.objects.get(pk = flight_id)
	except KeyError:
		return render(request,"frenebi/error.html", {"message":"KeyError"})
	except Flight.DoesNotExist:
		return render(request, "frenebi/error.html", {"message":"No Flight"})
	except Passenger.DoesNotExist:
		return render(request, "frenebi/error.html", {"message":"No Passenger"})

	passenger.reisi.add(flight)
	#in this line reverse()- gives you a url of 'frena' which id = flight_id
	return HttpResponseRedirect(reverse("frena", args=(flight_id,)))