from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from apps.groups.models import StudentGroup
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
    student_group = models.ForeignKey(StudentGroup, on_delete=models.PROTECT)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)
    limit_hour = models.PositiveSmallIntegerField(help_text='Time limit for the event')

    def __str__(self):
        return self.student_group


class ExamResult(models.Model):
    student = models.ForeignKey(CustomUser, limit_choices_to=CustomUser.RoleChoices.STUDENT.value,
                                on_delete=models.PROTECT)
    exam = models.ForeignKey(Exam, on_delete=models.SET_NULL, null=True)
    percent = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)],
                                help_text='Enter a percentage value between 0 and 100')
    comment = models.TextField(max_length=1500, blank=True)

    def __str__(self):
        return self.student