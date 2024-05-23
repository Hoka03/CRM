from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from apps.groups.models import Group
from apps.subjects.models import Subject
from apps.users.models import CustomUser


class Exam(models.Model):
    class MonthChoice(models.IntegerChoices):
        January = 1, 'January'
        February = 2, 'February'
        March = 3, 'March'
        April = 4, 'April'
        May = 5, 'May'
        June = 6, 'June'
        July = 7, 'July'
        August = 8, 'August'
        September = 9, 'September'
        October = 10, 'October'
        November = 11, 'November'
        December = 12, 'December'

    month = models.PositiveSmallIntegerField(choices=MonthChoice.choices, help_text='select the month')
    group = models.ForeignKey(Group, on_delete=models.PROTECT)
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)
    limit_hour = models.TimeField(help_text='Time limit for the event')

    def __str__(self):
        return self.group


class ExamResult(models.Model):
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    percent = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0),
                                                                              MaxValueValidator(100)],
                                  help_text='Enter a percentage value between 0 and 100')
    comment = models.TextField(max_length=1500)

    def __str__(self):
        return self.student