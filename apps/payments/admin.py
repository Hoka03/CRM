from django.contrib import admin

from apps.payments.models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('student', 'teacher', 'year', 'month', 'salary', 'in_percent', 'created_at')
    list_display_links = list_display

    def has_add_permission(self, request):
        return False
