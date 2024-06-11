from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

from apps.subjects.models import Subject


class Lesson(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    ordering_number = models.PositiveSmallIntegerField(default=1)
    content = CKEditor5Field('content', config_name='extends')

    def __str__(self):
        return self.title