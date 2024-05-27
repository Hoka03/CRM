from django.contrib import admin

from apps.users.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('role', 'gender', 'first_name', 'last_name', 'date_of_birth', 'date_joined', 'email',
                    'phone_number', 'address')
    list_display_links = list_display
