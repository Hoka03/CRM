from django.core.management import BaseCommand
from faker import Faker
from apps.users.models import CustomUser


class Command(BaseCommand):
    def handle(self, *args, **options):
        fake = Faker()

        for i in range(10):
            parents = CustomUser.objects.create(
                role=CustomUser.RoleChoices.PARENT.value,
                password=fake.password(),
                phone_number='+99899963{}65'.format(i + 85),
                email='parent{}@dd.com'.format(i + 78),
                gender=CustomUser.GenderChoices.MALE.value,
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                father_name=fake.first_name(),
                date_of_birth=fake.date_of_birth(),
                address=fake.address(),
                description=fake.text(354)
            ),
        self.stdout.write(self.style.SUCCESS(f'{len(parents)}-parents was created'))
