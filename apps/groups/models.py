from django.db import models
from django.contrib.postgres.fields import ArrayField

from apps.users.models import CustomUser


class StudentGroup(models.Model): # VALIDATE FOR TIME
    class WeekDay(models.IntegerChoices):
        MONDAY = 0, 'monday'
        TUESDAY = 1, 'tuesday'
        WEDNESDAY = 2, 'wednesday'
        THURSDAY = 3, 'thursday'
        FRIDAY = 4, 'friday'
        SATURDAY = 5, 'saturday'
        SUNDAY = 6, 'sunday'

    teacher = models.ForeignKey('users.CustomUser', limit_choices_to={'role': CustomUser.RoleChoices.TEACHER.value},
                                on_delete=models.PROTECT, related_name='group_teacher')
    subject = models.ForeignKey('subjects.Subject', on_delete=models.PROTECT, related_name='group_subject')
    start_time = models.TimeField()
    end_time = models.TimeField()
    week_day = ArrayField(base_field=models.PositiveSmallIntegerField(choices=WeekDay.choices))
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.teacher
