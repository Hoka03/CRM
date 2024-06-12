from django.contrib import admin

from apps.groups.models import StudentGroup


@admin.register(StudentGroup)
class StudentGroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'teacher', 'subject', 'start_time', 'end_time', 'week_day', 'created_at')
    list_display_links = list_display
