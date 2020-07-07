from django.views.generic import ListView, DetailView, View
from django.utils import timezone
from django.shortcuts import render
from django.core.paginator import Paginator
from . import models, forms


class HomeView(ListView):

    """ HomeView Definition """

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    page_kwarg = "page"
    context_object_name = "rooms"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context


class RoomDetail(DetailView):

    model = models.Room
    # pk_url_kwarg = 'mykey'


class SearchView(View):
    def get(self, request):
        country = request.GET.get("country")
        form = forms.SearchForm()

        if country:
            form = forms.SearchForm(request.GET)

            if form.is_valid():
                city = form.cleaned_data.get("city")
                country = form.cleaned_data.get("country")
                room_type = form.cleaned_data.get("room_type")
                price = form.cleaned_data.get("price")
                guests = form.cleaned_data.get("guests")
                bedrooms = form.cleaned_data.get("bedrooms")
                beds = form.cleaned_data.get("beds")
                baths = form.cleaned_data.get("baths")
                instant_book = form.cleaned_data.get("instant_book")
                superhost = form.cleaned_data.get("superhost")
                amenities = form.cleaned_data.get("amenities")
                facilities = form.cleaned_data.get("facilities")

                filter_args = {}

                if city != "Anywhere":
                    filter_args["city__startswith"] = city

                if country:
                    filter_args["country__exact"] = country

                if room_type is not None:
                    filter_args["room_type"] = room_type

                if price:
                    filter_args["price__lte"] = price

                if guests:
                    filter_args["guests__gte"] = guests

                if bedrooms:
                    filter_args["bedrooms__gte"] = bedrooms

                if beds:
                    filter_args["beds__gte"] = beds

                if baths:
                    filter_args["baths__gte"] = baths

                if instant_book:
                    filter_args["instant_book"] = True

                if superhost:
                    filter_args["host__superhost"] = True

                for amenity in amenities:
                    filter_args["amenities"] = amenity

                for facility in facilities:
                    filter_args["facilities"] = facility

                qs = models.Room.objects.filter(**filter_args).order_by("-created")

                paginator = Paginator(qs, 10, orphans=5)
                page = request.GET.get("page", 1)
                rooms = paginator.get_page(page)
                return render(
                    request, "rooms/search.html", {"form": form, "rooms": rooms},
                )
        # else:
        #     form = form.SearchForm()

        return render(request, "rooms/search.html", {"form": form})


# def search(request):


# from django.shortcuts import render
# from django.http import Http404
#
# def room_detail(request, pk):
#     try:
#         room = models.Room.objects.get(pk=pk)
#         return render(request, "rooms/detail.html", {
#             "room": room
#         })
#     except models.Room.DoesNotExist:
#         raise Http404()


# from django.shortcuts import render, redirect
# from django.core.paginator import Paginator, EmptyPage
#
# def all_rooms(request):
#     page = request.GET.get("page", 1)
#     room_list = models.Room.objects.all()
#     paginator = Paginator(room_list, 10, orphans=5)

#     try:
#         rooms = paginator.page(int(page))
#         return render(request, "rooms/home.html", {"page": rooms})
#     except EmptyPage:
#         return redirect("/")
