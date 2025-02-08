from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Booking

@receiver(post_delete, sender=Booking)
def update_room_availability(sender, instance, **kwargs):
    room = instance.room
    if not Booking.objects.filter(room=room).exists():
        room.is_available = True
        room.save()