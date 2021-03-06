from django.urls import path
from rooms import views as room_views

# namespace in config.urls
app_name = "core"

urlpatterns = [
    path("", room_views.HomeView.as_view(), name="home"),
]
