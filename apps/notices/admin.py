from django.contrib import admin

from apps.notices.models import Notification, Chat, ChatMessage


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('student', 'title', 'notification_type', 'is_viewed', 'content', 'exam_result', 'created_at',)
    list_display_links = list_display


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('recipient', 'sender', 'recipient_email', 'sender_email', 'recipient_phone_number',
                    'sender_phone_number', 'recipient_full_name', 'sender_full_name',)
    list_display_links = list_display
    fields = ('recipient', 'sender')


@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('chat', 'sender', 'message', 'created_at', 'viewed_at', 'is_viewed')