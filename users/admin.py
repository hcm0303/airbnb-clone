from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# from rooms import models as room_models


# class RoomInline(admin.StackedInline):
#    model = room_models.Room


# Register your models here.
@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """ Custom User Admin """

    # inline = (RoomInline,)

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                    "login_method",
                )
            },
        ),
    )

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "language",
        "currency",
        "superhost",
        "is_staff",
        "email_verified",
        "email_secret",
        "login_method",
    )

    list_filter = UserAdmin.list_filter + ("superhost",)
