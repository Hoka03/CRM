from django.db import models
from django.contrib.postgres.fields import ArrayField

from apps.users.models import CustomUser


class Group(models.Model):
    class WeekDay(models.IntegerChoices):
        MONDAY = 1, 'monday'
        TUESDAY = 2, 'tuesday'
        WEDNESDAY = 3, 'wednesday'
        THURSDAY = 4, 'thursday'
        FRIDAY = 5, 'friday'
        SATURDAY = 6, 'saturday'
        SUNDAY = 7, 'sunday'

    teacher = models.ForeignKey('users.CustomUser', limit_choices_to={'role': CustomUser.RoleChoices.TEACHER.value},
                                on_delete=models.PROTECT, related_name='group_teacher')
    subject = models.ForeignKey('subjects.Subject', on_delete=models.PROTECT, related_name='group_subject')
    gender = models.ForeignKey('users.CustomUser', limit_choices_to={'gender': CustomUser.GenderChoices.MALE.value},
                               on_delete=models.CASCADE, related_name='group_gender')
    start_time = ArrayField(models.CharField(max_length=5))
    end_time = ArrayField(models.CharField(max_length=5))
    week_day = ArrayField(base_field=models.PositiveSmallIntegerField(choices=WeekDay.choices))
    created_day = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.teacher
