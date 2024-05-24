from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import ValidationError

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

    USERNAME = None

    objects = CustomUserManager()

    role = models.PositiveSmallIntegerField(choices=RoleChoices.choices)
    gender = models.PositiveSmallIntegerField(choices=GenderChoices.choices)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    father_name = models.CharField(max_length=150)
    mother_name = models.CharField(max_length=150, blank=True)
    date_of_birth = models.DateField()
    joining_data = models.DateField(auto_now_add=True)
    email = models.EmailField(unique=True)
    # SALARY ADD, WHEN TEACHER WAS CREATED
    salary = models.DecimalField(max_digits=20, decimal_places=2, default=0,
                                 help_text='Add in UZS')
    # GROUP ADD, WHEN STUDENT WAS CREATED
    student_group = models.ForeignKey('groups.StudentGroup', on_delete=models.CASCADE, related_name='user_group',
                                      blank=True, null=True)
    # CHILD ADD, WHEN PARENT WAS CREATED
    child = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    phone_number = models.CharField(max_length=13, validators=[phone_validate], unique=True)
    address = models.CharField(max_length=150)

    def clean(self):
        #   FOR TEACHER
        super().clean()
        if self.role == self.RoleChoices.TEACHER and self.salary == 0:
            raise ValidationError('Salary must be provided for teacher')
        #   FOR STUDENT
        super().clean()
        if self.role == self.RoleChoices.STUDENT and self.student_group == 0:
            raise ValidationError('StudentGroup must be provided for student')

        # FOR PARENTS
        super().clean()
        if self.role == self.RoleChoices.PARENT and self.child == 0:
            raise ValidationError('Child must be provided for Parent')

    def __str__(self):
        return self.role

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['role', 'email', 'first_name', 'last_name']

    @classmethod
    def get_normalize_fields(cls):
        return [
            'first_name'
            'last_name'
            'father_name'
            'mother_name'
        ]

    def save(self, *args, **kwargs):
        normalize_text(self)
        super().save(*args, **kwargs)