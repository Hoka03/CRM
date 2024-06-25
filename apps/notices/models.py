from django.db import models
from django.conf import settings

from apps.general.services import normalize_text
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


    #if type == EXAM_RESULT
    #FOR PARENTS TOO
    student = models.ForeignKey(settings.AUTH_USER_MODEL, limit_choices_to=Type.EXAM_RESULT.value,
                                on_delete=models.CASCADE)
    exam_result = models.ForeignKey('exams.ExamResult', on_delete=models.CASCADE)


class Message(models.Model):
    from_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
                                  null=True, related_name='from_messages')
    to_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
                                null=True, related_name='to_messages')
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_viewed = models.BooleanField(default=False)

    from_user_email = models.CharField(max_length=255)
    from_user_phone_number = models.CharField(max_length=13, validators=[phone_validate])
    from_user_full_name = models.CharField(max_length=255)

    to_user_email = models.CharField(max_length=255)
    to_user_phone_number = models.CharField(max_length=13, validators=[phone_validate])
    to_user_full_name = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        self.from_user_email = self.from_user.email
        self.from_user_phone_number = self.from_user.phone_number
        self.from_user_full_name = self.from_user.get_full_name()
        self.to_user_email = self.to_user.email
        self.to_user_phone_number = self.to_user.phone_number
        self.to_user_full_name = self.to_user.get_full_name()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.message}'
