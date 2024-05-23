from django.db import models

from apps.users.models import CustomUser


class Attendance(models.Model):
    class StatusChoice(models.TextChoices):
        COME = 1, 'come'
        DID_NOT_COME = 2, 'did not come'
        REASON = 3, 'reason'
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    attendance_date = models.DateField()
    status = models.PositiveSmallIntegerField(choices=StatusChoice.choices)
    reason = models.CharField(max_length=150)

    class Meta:
        unique_together = ('student', 'attendance_date')

    def __str__(self):
        return f'{self.student} on {self.date}'
