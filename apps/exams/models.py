from django.db import models
from django.db.models import Q
from django.core.validators import MinValueValidator, MaxValueValidator

from apps.subjects.models import Subject
from apps.users.models import CustomUser
from apps.general.services import normalize_text
from apps.general.enums.months import MonthChoice
from ..general.models import AbstractModel


class Exam(AbstractModel):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    nth_month = models.PositiveSmallIntegerField(choices=MonthChoice.choices, help_text='select the month')
    limit_hour = models.PositiveSmallIntegerField(help_text='Time limit for the event, In hour')

    def __str__(self):
        return f"{self.subject}"

    class Meta:
        unique_together = ('subject', 'nth_month')


class ExamResult(models.Model):
    student = models.ForeignKey(CustomUser, limit_choices_to=Q(role=CustomUser.RoleChoices.STUDENT.value),
                                on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.PROTECT, null=True)
    percent = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)],
                                help_text='Enter a percentage value between 0 and 100')
    comment = models.TextField(max_length=1500, blank=True)

    def __str__(self):
        return str(self.student)


