from django.core.management import BaseCommand
from apps.users.models import CustomUser
from django.utils.timezone import now


class Command(BaseCommand):
    def handle(self, *args, **options):
        phone_number = input('phone_number: ')
        password = input('password: ')
        while True:
            username = input('username: ')
            if not CustomUser.objects.filter(username=username).exists():
                break
            self.stdout.write(self.style.ERROR(f"Username '{username}',"
                                               f" already exists. Please choose a different username."))

        admin = CustomUser.objects.create_superuser(
            role=1,
            phone_number=phone_number,
            email='a@a.aa',
            gender=1,
            first_name='Henry',
            last_name='Morgan',
            father_name='Robert Morgan',
            date_of_birth=now().date(),
            address='Port Royal',
            password=password,
            username=username
        )
        self.stdout.write(self.style.SUCCESS(f"{admin} Was created successfully."))
