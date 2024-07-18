from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Room(models.Model):
    ROOM_TYPES = [
        ('single', '1 комната'),
        ('double', '2 комната'),
        ('suite', 'президентский'),
    ]

    room_number = models.CharField(max_length=50)
    room_type = models.CharField(max_length=10, choices=ROOM_TYPES)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    photo = models.ImageField(upload_to='room_photos/')

    def __str__(self):
        return f'номер {self.room_number} ({self.get_room_type_display()})'


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()

    def __str__(self):
        return f'бронь №{self.id} - {self.room} для {self.user.username}'
