from django.core.management import BaseCommand
from faker import Faker

from apps.users.models import CustomUser


class Command(BaseCommand):
    def handle(self, *args, **options):
        fake = Faker()

        for i in range(10):
            students = CustomUser.objects.create(
                role=CustomUser.RoleChoices.STUDENT.value,
                password=fake.password(),
                phone_number='+9989785263{}'.format(i + 80),
                email='student{}@dd.com'.format(i + 200),
                gender=CustomUser.GenderChoices.MALE.value,
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                father_name=fake.first_name(),
                date_of_birth=fake.date_of_birth(),
                address=fake.address(),
                description=fake.texts(max_nb_chars=350)
            ),
        self.stdout.write(self.style.SUCCESS(f"{len(students)}-students was created."))
