import datetime
from django.db import models
from django.db.models import Q
from django.contrib.postgres.fields import ArrayField
from django.core.validators import ValidationError
from django.conf import settings


from apps.users.models import CustomUser
from apps.general.enums.weeks import WeekDay


class StudentGroup(models.Model):
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, limit_choices_to={'role': CustomUser.RoleChoices.TEACHER.value},
                                on_delete=models.PROTECT, related_name='teacher_groups')
    subject = models.ForeignKey('subjects.Subject', on_delete=models.PROTECT, related_name='subject_groups')
    start_time = models.TimeField()
    end_time = models.TimeField()
    week_day = ArrayField(base_field=models.PositiveSmallIntegerField(choices=WeekDay.choices))
    created_at = models.DateField(auto_now_add=True)

    def clean(self):
        if self.end_time <= self.start_time:
            raise ValidationError({'end_time': 'End time must be greater than Start time.'})

        if StudentGroup.objects.filter(teacher_id=self.teacher.pk, week_day=self.week_day).filter(
                Q(start_time__range=(self.start_time, self.end_time))
                |
                Q(end_time__range=(self.start_time, self.end_time))
        ).exists():
            raise ValidationError(f'{self.teacher}`s have not time between {self.start_time}, {self.end_time}')

    def __str__(self):
        return f'{self.subject}: {self.start_time} - {self.end_time}'


