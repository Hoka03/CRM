from django.db import models
from django.contrib.auth.models import AbstractUser

from apps.general.validations import phone_validate
from apps.users.managers import CustomUserManager
from apps.general.services import normalize_text
from apps.subjects.models import Subject


class CustomUser(AbstractUser):
    class RoleChoices(models.TextChoices):
        ADMIN = 'admin', 'admin'
        TEACHER = 'teacher', 'teacher'
        STUDENT = 'student', 'student'
        PARENTS = 'parents', 'parents'

    class GenderChoices(models.TextChoices):
        MALE = 'male', 'male'
        FEMALE = 'female', 'female'

    USERNAME = None

    objects = CustomUserManager

    role = models.CharField(max_length=10, choices=RoleChoices.choices)
    gender = models.CharField(max_length=50, choices=GenderChoices.choices)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    father_name = models.CharField(max_length=150)
    mother_name = models.CharField(max_length=150)
    date_of_birth = models.DateTimeField()
    religion = models.CharField(max_length=150)
    joining_data = models.DateField(auto_now_add=True)
    email = models.EmailField(max_length=150)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    group = models.ForeignKey('groups.Group', on_delete=models.CASCADE, related_name='user_group')
    section = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13, validators=[phone_validate], unique=True)
    address = models.CharField(max_length=150)

    def __str__(self):
        return self.role

    USERNAME_FIELD = 'phone_number'

    def get_normalize_fields(self):
        return [
            'first_name'
            'last_name'
            'father_name'
            'mother_name'
        ]

    def save(self, *args, **kwargs):
        normalize_text(self)
        super().save(*args, **kwargs)