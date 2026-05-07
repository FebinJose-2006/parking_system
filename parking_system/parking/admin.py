from django.contrib import admin
from .models import ParkingLot, Slot, Booking

admin.site.register(ParkingLot)
admin.site.register(Slot)
admin.site.register(Booking)