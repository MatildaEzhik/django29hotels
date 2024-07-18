from django.contrib import admin

from hotels.models import Room, Booking

# Register your models here.

admin.site.register(Room)
admin.site.register(Booking)