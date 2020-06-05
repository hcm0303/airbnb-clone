from django.shortcuts import render
from . import models


# Create your views here.
def all_rooms(request):
    all_rooms = models.Room.objects.all()
    # print(dir(request))
    # print(vars(request))
    return render(request, "rooms/home.html", context={"rooms": all_rooms})
