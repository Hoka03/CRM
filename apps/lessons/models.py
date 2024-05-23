from django.db import models

from apps.subjects.models import Subject


class Lesson(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    ordering_number = models.CharField(max_length=150)

    def __str__(self):
        return self.subject