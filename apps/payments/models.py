from django.db import models

from apps.users.models import CustomUser
from apps.general.validations import phone_validate


class Payment(models.Model):
    student = models.ForeignKey(CustomUser, on_delete=models.PROTECT, related_name='payment_student')
    teacher = models.ForeignKey(CustomUser, on_delete=models.PROTECT, related_name='payment_teacher')
    salary = models.DecimalField(max_digits=20, decimal_places=2, help_text='Add in UZS')
    in_percent = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=13, validators=[phone_validate])
    email = models.EmailField(max_length=150)
    # year
    # month

    def __str__(self):
        if self.teacher:
            return self.teacher
        elif self.student:
            return self.student

