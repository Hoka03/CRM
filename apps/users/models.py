from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import ValidationError, MinValueValidator

from apps.general.validations import phone_validate
from apps.users.managers import CustomUserManager
from apps.general.services import normalize_text


class CustomUser(AbstractUser):
    class RoleChoices(models.IntegerChoices):
        ADMIN = 1, 'admin'
        TEACHER = 2, 'teacher'
        STUDENT = 3, 'student'
        PARENT = 4, 'parent'

    class GenderChoices(models.IntegerChoices):
        MALE = 1, 'male'
        FEMALE = 2, 'female'

    username = None

    objects = CustomUserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    role = models.PositiveSmallIntegerField(choices=RoleChoices.choices)
    gender = models.PositiveSmallIntegerField(choices=GenderChoices.choices, blank=True, null=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    father_name = models.CharField(max_length=150)
    mother_name = models.CharField(max_length=150, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    email = models.EmailField(unique=True)

    # SALARY ADD, WHEN TEACHER WAS CREATED
    salary = models.DecimalField(max_digits=20, decimal_places=2, default=0,
                                 help_text='Add in UZS',
                                 validators=[MinValueValidator(0)])

    # GROUP ADD, WHEN STUDENT WAS CREATED
    student_group = models.ForeignKey('groups.StudentGroup', on_delete=models.CASCADE, related_name='students',
                                      blank=True, null=True)

    # CHILD ADD, WHEN PARENT WAS CREATED
    child = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    phone_number = models.CharField(max_length=13, validators=[phone_validate], unique=True)
    address = models.CharField(max_length=150)

    def clean(self):
        #   FOR TEACHER
        super().clean()
        if self.role == self.RoleChoices.TEACHER.value and self.salary is None:
            raise ValidationError({'salary': 'Salary must be provided for teacher'})

        #   FOR STUDENT
        if self.role == self.RoleChoices.STUDENT.value and self.student_group is None:
            raise ValidationError({'student_group': 'StudentGroup must be provided for student'})

        # FOR PARENTS
        if self.role == self.RoleChoices.PARENT.value and self.child is None:
            raise ValidationError({'child': 'Child must be provided for Parent'})

    def __str__(self):
        return f"{self.get_role_display()} {self.email}"

    @classmethod
    def get_normalize_fields(cls):
        return ['first_name', 'last_name', 'father_name', 'mother_name']

    def save(self, *args, **kwargs):
        normalize_text(self)
        super().save(*args, **kwargs)