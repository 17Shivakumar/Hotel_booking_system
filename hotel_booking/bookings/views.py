from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Hotel, Room, Booking
from .forms import BookingForm


def hotel_list(request):
    location_query = request.GET.get('location', '')
    availability = request.GET.get('availability', False)

    hotels = Hotel.objects.all()
    if location_query:
        hotels = hotels.filter(location__icontains=location_query)

    for hotel in hotels:
        rooms = hotel.room_set.all()
        if availability:
            rooms = rooms.filter(is_available=True)
        hotel.available_rooms = rooms

    return render(request, 'bookings/hotel_list.html', {
        'hotels': hotels,
        'location_query': location_query,
        'availability': availability,
    })


def book_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            check_in = form.cleaned_data['check_in']
            check_out = form.cleaned_data['check_out']

            if not room.is_available:
                messages.error(request, 'This room is not available.')
                return redirect('book_room', room_id=room.id)

            overlapping_bookings = Booking.objects.filter(
                room=room,
                check_out__gt=check_in,
                check_in__lt=check_out
            )
            if overlapping_bookings.exists():
                messages.error(request, 'Room already booked for these dates')
                return redirect('book_room', room_id=room.id)

            booking = form.save(commit=False)
            booking.room = room
            booking.hotel = room.hotel
            booking.save()

            room.is_available = False
            room.save()

            messages.success(request, 'Booking successful!')
            return redirect('booking_confirmation', booking_id=booking.id)
    else:
        form = BookingForm()

    return render(request, 'bookings/book_room.html', {
        'form': form,
        'room': room,
    })


def booking_confirmation(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, 'bookings/booking_confirmation.html', {'booking': booking})