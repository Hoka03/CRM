from django.core.management import BaseCommand
from django.db.models import Q

from apps.users.models import CustomUser
from django.utils.timezone import now


class Command(BaseCommand):
    def handle(self, *args, **options):
        password = input('password: ')
        while True:
            email = input('email: ')
            phone_number = input('phone_number: ')
            if not CustomUser.objects.filter(Q(email=email) | Q(phone_number=phone_number)).exists():
                break
            self.stdout.write(self.style.ERROR(f"Username '{email}',"
                                               f" already exists. Please choose a different username."))

        admin = CustomUser.objects.create_superuser(
            role=1,
            phone_number=phone_number,
            gender=1,
            first_name='Henry',
            last_name='Morgan',
            father_name='Robert Morgan',
            date_of_birth=now().date(),
            address='Port Royal',
            password=password,
            email=email
        )
        self.stdout.write(self.style.SUCCESS(f"{admin} Was created successfully."))
