from django.contrib import admin
from .models import Hotel, Room, Booking

class BookingAdmin(admin.ModelAdmin):
    list_display = ('hotel', 'room', 'customer_name', 'check_in', 'check_out')
    list_filter = ('hotel',)
    search_fields = ('customer_name', 'room__room_number')

admin.site.register(Hotel)
admin.site.register(Room)
admin.site.register(Booking, BookingAdmin)