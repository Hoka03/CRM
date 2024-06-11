from django.contrib import admin

from apps.attendances.models import Attendance


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'attendance_date', 'status', 'reason')
    list_display_links = list_display
