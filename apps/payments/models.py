from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, ValidationError

from apps.users.models import CustomUser


class Payment(models.Model):
    student = models.ForeignKey(CustomUser, limit_choices_to={'role': CustomUser.RoleChoices.STUDENT.value},
                                on_delete=models.PROTECT, related_name='payment_student', blank=True, null=True)
    teacher = models.ForeignKey(CustomUser, limit_choices_to={'role': CustomUser.RoleChoices.TEACHER.value},
                                on_delete=models.PROTECT, related_name='payment_teacher', blank=True, null=True)
    year = models.PositiveIntegerField()
    month = models.PositiveIntegerField()
    salary = models.DecimalField(max_digits=20, decimal_places=2, help_text='Add in UZS')
    in_percent = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)],
                                                  help_text='Before add in_percent, look at role.')
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if (bool(self.student) + bool(self.teacher)) != 1:
            raise ValidationError('Here you must add Teacher or Student.')

    class Meta:
        unique_together = (('year', 'month', 'student'), ('year', 'month', 'teacher'))

    def __str__(self):
        if self.teacher:
            return f'{self.salary}: {self.in_percent}'
        elif self.student:
            return f'{self.salary}: {self.in_percent}'

