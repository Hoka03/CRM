from django.db import models
from django.conf import settings

from apps.general.validations import phone_validate


class Notification(models.Model):
    class Type(models.IntegerChoices):
        EXAM_RESULT = 0, 'exam result'  # himself
        ON_ATTENDANCE = 1, 'on attendance'  # for parent
        ON_PAYMENT = 2, 'payment time'  # parent and himself
        WARNING = 3, 'Warning'  # for all

    title = models.PositiveSmallIntegerField(choices=Type.choices)
    notification_type = models.PositiveSmallIntegerField(choices=Type.choices)
    is_viewed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=455, blank=True)

    def clean(self):
        if self.Type == (self.Type.EXAM_RESULT and self.Type.ON_PAYMENT and self.Type.ON_PAYMENT):
            pass

    # if type == EXAM_RESULT
    # FOR PARENTS TOO
    student = models.ForeignKey(settings.AUTH_USER_MODEL, limit_choices_to=Type.EXAM_RESULT.value,
                                on_delete=models.CASCADE)
    exam_result = models.ForeignKey('exams.ExamResult', on_delete=models.CASCADE)


class Chat(models.Model):
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
                                  null=True, related_name='from_messages')
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
                               null=True, related_name='to_messages')

    recipient_email = models.CharField(max_length=255)
    recipient_phone_number = models.CharField(max_length=13, validators=[phone_validate])
    recipient_full_name = models.CharField(max_length=255)

    sender_email = models.CharField(max_length=255)
    sender_phone_number = models.CharField(max_length=13, validators=[phone_validate])
    sender_full_name = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        if self.recipient:
            self.recipient_email = self.recipient.email
            self.recipient_phone_number = self.recipient.phone_number
            self.recipient_full_name = self.recipient.get_full_name()

        if self.sender:
            self.sender_email = self.sender.email
            self.sender_phone_number = self.sender.phone_number
            self.sender_full_name = self.sender.get_full_name()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.recipient} - {self.sender}'


class ChatMessage(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

    message = models.CharField(max_length=255)
    is_viewed = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    viewed_at = models.DateTimeField(blank=True, null=True)

    image = models.ImageField(upload_to='chat/', blank=True, null=True)

    def __str__(self):
        return f'{self.sender} {self.chat.id}'
