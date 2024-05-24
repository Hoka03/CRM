from django.contrib import admin

from apps.notices.models import Notification, Message


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'details', 'created_at')
    list_display_links = list_display
    prepopulated_fields = {'slug': ['title']}


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('from_user', 'to_user', 'title', 'slug', 'message')
    list_display_links = list_display
    list_select_related = ('from_user', 'to_user')
    prepopulated_fields = {'slug': ['title']}
