from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import CustomUser
# Register your models here.


class CustomUserAdmin(UserAdmin):
    # add form = where you'd create a custom form class to the admin if you
    # needed custom attributes
    # form =
    model = CustomUser
    list_display = ["username", "email", "is_staff"]


admin.site.register(CustomUser, CustomUserAdmin)
