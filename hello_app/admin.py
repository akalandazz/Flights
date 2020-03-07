from django.contrib import admin
from .models import AirPort, Flight, Passenger
# Register your models here.

'''
StackedInline is django builtin class which 
lets us to add stacked relationship between
objects, it represents place of the admin inteface 
where i will be able to add and modify passengers
'''

class PassengerInline(admin.StackedInline):
	#it connects individual passenger to individual flights
	model = Passenger.reisi.through 
	extra = 1

class FlightAdmin(admin.ModelAdmin):
	inlines = [PassengerInline]

#we extend features of this modeladmin class, so we can add features 
#it's a special configuration of settings 
class PassengerAdmin(admin.ModelAdmin):
	filter_horizontal = ("reisi",)
	#filter_horizontal- is built-in function


admin.site.register(AirPort)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Passenger, PassengerAdmin)
#when i registered Passenger i told that use PassengerAdmin feature
#which contains additional features