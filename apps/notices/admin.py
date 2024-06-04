from django.contrib import admin

from apps.notices.models import Notification, Message


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('student', 'title', 'notification_type', 'is_viewed', 'content', 'exam_result', 'created_at',)
    list_display_links = list_display


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('from_user', 'to_user', 'message', 'from_user_email', 'to_user_email', 'from_user_phone_number',
                    'to_user_phone_number', 'from_user_full_name', 'to_user_full_name',)
    list_display_links = list_display
