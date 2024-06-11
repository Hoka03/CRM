from django.core.management.base import BaseCommand
from django.utils import timezone
from decimal import Decimal


from apps.payments.models import Payment
from apps.users.models import CustomUser


class Command(BaseCommand):
    def handle(self, *args, **options):
        created_time_1 = timezone.datetime(2024, 6, 15, 10, 30, 0)
        created_time_2 = timezone.datetime(2024, 4, 20, 12, 45, 10)
        created_time_3 = timezone.datetime(2024, 9, 25, 14, 55, 20)

        payments = [
            Payment(
                student_id=CustomUser.objects.get(first_name="Robert").id,
                year=2024,
                month=6,
                salary=Decimal('1200000'),
                in_percent=60,
                created_at=created_time_1
            ),

            Payment(
                teacher_id=CustomUser.objects.get(first_name="Edna").id,
                year=2024,
                month=4,
                salary=Decimal('3400000'),
                in_percent=80,
                created_at=created_time_2
            ),

            Payment(
                teacher_id=CustomUser.objects.get(first_name="Edna").id,
                year=2024,
                month=9,
                salary=Decimal('5600000'),  
                in_percent=85,
                created_at=created_time_3
            ),
        ]
        Payment.objects.bulk_create(payments)
        self.stdout.write(self.style.SUCCESS(f'{len(payments)} payments were created.'))
