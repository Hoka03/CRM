from django.db import models
from django.conf import settings

from apps.users.models import CustomUser


class Attendance(models.Model):
    class StatusChoice(models.TextChoices):
        COME = 'come', 'Come'
        DID_NOT_COME = 'did_not_come', 'Did not come'
        REASON = 'reason', 'Reason'

    student = models.ForeignKey(settings.AUTH_USER_MODEL,
                                limit_choices_to={'role': CustomUser.RoleChoices.STUDENT.value},
                                on_delete=models.CASCADE)
    attendance_date = models.DateField()
    status = models.CharField(max_length=50, choices=StatusChoice.choices)
    reason = models.CharField(max_length=150, blank=True)

    class Meta:
        unique_together = ('student', 'attendance_date')

    def __str__(self):
        return f'{self.student}'

