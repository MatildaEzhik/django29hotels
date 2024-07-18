from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from hotels.forms import RoomForm, BookingForm
from hotels.models import Room, Booking


def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'hotels29/room_list.html', {'rooms': rooms})

def room_detail(request, pk):
    room = Room.objects.get(pk=pk)
    return render(request, 'hotels29/room_detail.html', {'room': room})

@login_required
def room_create(request):
    if request.method == 'POST':
        form = RoomForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('room_list')
    else:
        form = RoomForm()
    return render(request, 'hotels29/room_form.html', {'form': form})

@login_required
def room_edit(request, pk):
    room = Room.objects.get(pk=pk)
    if request.method == 'POST':
        form = RoomForm(request.POST, request.FILES, instance=room)
        if form.is_valid():
            form.save()
            return redirect('room_list')
    else:
        form = RoomForm(instance=room)
    return render(request, 'hotels29/room_form.html', {'form': form})

@login_required
def room_delete(request, pk):
    room = Room.objects.get(pk=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('room_list')
    return render(request, 'hotels29/room_confirm_delete.html', {'room': room})

@login_required
def booking_create(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('booking_list')
    else:
        form = BookingForm()
    return render(request, 'hotels29/booking_form.html', {'form': form})

@login_required
def booking_list(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'hotels29/booking_list.html', {'bookings': bookings})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'hotels/templates/sign_up.html', {'form': form})
