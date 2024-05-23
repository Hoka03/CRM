from django.db import models


from apps.users.models import CustomUser


class Attendance(models.Model):
    class Status(models.TextChoices):
        PLUS = 'plus', 'plus'
        MINUS = 'minus', 'minus'
        TICKED = 'ticked', 'ticked'
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=100, choices=Status.choices)

    def __str__(self):
        return self.student