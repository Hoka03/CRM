from django.contrib import admin

from apps.users.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('role', 'gender', 'first_name', 'last_name', 'father_name', 'mother_name', 'date_of_birth',
                    'date_joined', 'email',
                    'phone_number', 'address')

    list_display_links = list_display

    readonly_fields = ['date_joined', 'last_login']

    # fieldsets = [('Name', {'fields': ['first_name', 'last_name', 'email', 'father_name', 'mother_name']}),
    #              ('Auth', {'fields': ['role', 'gender', 'student_group', 'date_of_birth', 'date_joined', 'phone_number',
    #                                   'address']})]

    def save_model(self, request, obj, form, change):
        if not obj.pk or not obj.check_password(obj.password):
            obj.set_password(obj.password)
        obj.save()