from django.db import models
from django.conf import settings

from apps.users.models import CustomUser
from apps.general.services import normalize_text


class Attendance(models.Model):
    class StatusChoice(models.IntegerChoices):
        COME = 1, 'come'
        DID_NOT_COME = 2, 'did not come'
        REASON = 3, 'reason'

    student = models.ForeignKey(settings.AUTH_USER_MODEL,
                                limit_choices_to={'role': CustomUser.RoleChoices.STUDENT.value},
                                on_delete=models.CASCADE)
    attendance_date = models.DateField()
    status = models.PositiveSmallIntegerField(choices=StatusChoice.choices)
    reason = models.CharField(max_length=150, blank=True)

    class Meta:
        unique_together = ('student', 'attendance_date')

    def __str__(self):
        return f'{self.student}'

    @classmethod
    def get_normalize_fields(cls):
        return ['reason']

    def save(self, *args, **kwargs):
        normalize_text(self)
        super().save(*args, **kwargs)