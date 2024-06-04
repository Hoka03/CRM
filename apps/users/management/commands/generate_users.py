from django.core.management import BaseCommand
from django.utils import timezone
from apps.users.models import CustomUser
from django.utils.text import slugify


class Command(BaseCommand):
    def handle(self, *args, **options):
        created_time_1 = timezone.datetime(1960, 3, 23, 10, 30, 0)
        created_time_2 = timezone.datetime(1890, 1, 16, 12, 45, 10)
        created_time_3 = timezone.datetime(1635, 7, 18, 14, 55, 20)

        users = [
            CustomUser(
                username=slugify('Abraham Lincoln'),
                role=CustomUser.RoleChoices.ADMIN,
                phone_number='+998999639865',
                email='admin1@dd.com',
                gender=CustomUser.GenderChoices.MALE,
                first_name='Abraham',
                last_name='Lincoln',
                father_name='Henry Morgan',
                date_of_birth=created_time_1,
                address='The Gettysburg Address',
            ),

            CustomUser(
                username=slugify('Edna Francis'),
                role=CustomUser.RoleChoices.TEACHER,
                phone_number='+998904561263',
                email='teacher1@dd.com',
                gender=CustomUser.GenderChoices.FEMALE,
                first_name='Edna',
                last_name='Francis',
                father_name='Edward S.',
                date_of_birth=created_time_2,
                address='205 South Water Street North_field,',
            ),

            CustomUser(
                username=slugify('Robert Hooke'),
                role=CustomUser.RoleChoices.STUDENT,
                phone_number='+998978526341',
                email='student1@dd.com',
                gender=CustomUser.GenderChoices.MALE,
                first_name='Robert',
                last_name='Hooke',
                father_name='Edward S.',
                date_of_birth=created_time_3,
                address=' Isle of Wight',
            ),
        ]
        CustomUser.objects.bulk_create(users)
        self.stdout.write(self.style.SUCCESS(f'{len(users)} users were created.'))
