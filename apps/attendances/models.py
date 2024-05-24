from django.db import models

from apps.users.models import CustomUser
from apps.general.services import normalize_text


class Attendance(models.Model):
    class StatusChoice(models.IntegerChoices):
        COME = 1, 'come'
        DID_NOT_COME = 2, 'did not come'
        REASON = 3, 'reason'
    student = models.ForeignKey(CustomUser, limit_choices_to={'role': CustomUser.RoleChoices.STUDENT.value},
                                on_delete=models.CASCADE)
    attendance_date = models.DateField()
    status = models.PositiveSmallIntegerField(choices=StatusChoice.choices)
    reason = models.CharField(max_length=150)

    class Meta:
        unique_together = ('student', 'attendance_date')

    def __str__(self):
        return f'{self.student} on {self.attendance_date}'

    @classmethod
    def get_normalize_text(cls):
        return ['reason']

    def save(self, *args, **kwargs):
        normalize_text(self)
        super().save(*args, **kwargs)