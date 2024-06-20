from django.core.management.base import BaseCommand
from django.utils import timezone
from decimal import Decimal
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist

from apps.payments.models import Payment
from apps.users.models import CustomUser


class Command(BaseCommand):
    def handle(self, *args, **options):
        created_time_1 = timezone.datetime(2024, 6, 15, 10, 30, 0)
        created_time_2 = timezone.datetime(2024, 4, 20, 12, 45, 10)
        created_time_3 = timezone.datetime(2024, 9, 25, 14, 55, 20)

        def get_user_by_first_name(first_name):
            try:
                return CustomUser.objects.get(first_name=first_name).id
            except MultipleObjectsReturned:
                return CustomUser.objects.filter(first_name=first_name).first().id
            except ObjectDoesNotExist:
                self.stdout.write(self.style.ERROR(f'No user found with first name: {first_name}'))
                return None

        payments = [
            Payment(
                student_id=get_user_by_first_name("Robert"),
                year=2024,
                month=6,
                salary=Decimal('1200000'),
                in_percent=60,
                created_at=created_time_1
            ),
            Payment(
                student_id=get_user_by_first_name("Holy"),
                year=2024,
                month=2,
                salary=Decimal('125400'),
                in_percent=65,
                created_at=created_time_2
            ),
            Payment(
                student_id=get_user_by_first_name("Alex"),
                year=2024,
                month=4,
                salary=Decimal('650000'),
                in_percent=80,
                created_at=created_time_3
            ),
            Payment(
                teacher_id=get_user_by_first_name("Edna"),
                year=2024,
                month=4,
                salary=Decimal('3400000'),
                in_percent=80,
                created_at=created_time_1
            ),
            Payment(
                teacher_id=get_user_by_first_name("Holy"),
                year=2023,
                month=6,
                salary=Decimal('320000'),
                in_percent=82,
                created_at=created_time_2
            ),
            Payment(
                teacher_id=get_user_by_first_name("Miya"),
                year=2024,
                month=5,
                salary=Decimal('654000'),
                in_percent=79,
                created_at=created_time_3
            ),
        ]

        payments = [payment for payment in payments if payment.student_id or payment.teacher_id]
        Payment.objects.bulk_create(payments)
        self.stdout.write(self.style.SUCCESS(f'{len(payments)} payments were created.'))
