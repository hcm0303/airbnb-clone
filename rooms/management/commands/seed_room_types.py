from django.core.management.base import BaseCommand
from rooms.models import RoomType


class Command(BaseCommand):

    help = "This command creates roomTypes"

    def handle(self, *args, **options):
        room_types = [
            "House",
            "Apartment",
            "GuestHouse",
            "Hotel",
            "Cottage"
        ]
        for a in room_types:
            RoomType.objects.create(name=a)

        self.stdout.write(self.style.SUCCESS("RoomTypes created!"))