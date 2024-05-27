from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

from apps.subjects.models import Subject


class Lesson(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    ordering_number = models.CharField(max_length=150)
    content = RichTextUploadingField(config_name='design')

    def __str__(self):
        return self.title