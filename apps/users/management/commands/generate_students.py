from django.core.management import BaseCommand
from faker import Faker
from apps.users.models import CustomUser
from apps.groups.models import StudentGroup


class Command(BaseCommand):
    def handle(self, *args, **options):
        fake = Faker()

        student_group_ids = list(StudentGroup.objects.values_list('id', flat=True))

        if not student_group_ids:
            self.stdout.write(self.style.ERROR("No student groups available."))
            return

        students_created = 0

        for i in range(10):
            student_group_id = student_group_ids[i % len(student_group_ids)]

            CustomUser.objects.create(
                role=CustomUser.RoleChoices.STUDENT.value,
                password=fake.password(),
                phone_number='+9989785263{}'.format(i + 80),
                email='student{}@dd.com'.format(i + 200),
                student_group_id=student_group_id,
                gender=CustomUser.GenderChoices.MALE.value,
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                father_name=fake.first_name(),
                date_of_birth=fake.date_of_birth(),
                address=fake.address(),
                description=fake.text(max_nb_chars=350)
            )
            students_created += 1

        self.stdout.write(self.style.SUCCESS(f"{students_created} students were created."))
