from django.core.management import BaseCommand
from faker import Faker

from apps.users.models import CustomUser


class Command(BaseCommand):
    def handle(self, *args, **options):
        faker = Faker()

        for i in range(10):
            teachers = CustomUser.objects.create(
                role=CustomUser.RoleChoices.TEACHER.value,
                password=faker.password(),
                phone_number='+9989045612{}'.format(i + 50),
                email='teacher{}@dd.com'.format(i + 150),
                gender=CustomUser.GenderChoices.FEMALE.value,
                first_name='Edna{i}',
                last_name=faker.last_name(),
                father_name=faker.last_name(),
                date_of_birth=faker.date_of_birth(),
                address=faker.address(),
                description=faker.text(250)
            ),
        self.stdout.write(self.style.SUCCESS(f"{len(teachers)}-teachers was created."))
