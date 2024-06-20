from django.core.management import BaseCommand
from django.utils import timezone
from apps.users.models import CustomUser


class Command(BaseCommand):
    def handle(self, *args, **options):
        created_time_1 = timezone.datetime(1960, 3, 23, 10, 30, 0)
        created_time_2 = timezone.datetime(1890, 1, 16, 12, 45, 10)
        created_time_3 = timezone.datetime(1635, 7, 18, 14, 55, 20)

        users = [
            CustomUser(
                role=CustomUser.RoleChoices.PARENT.value,
                phone_number='+998999639865',
                email='parent1@dd.com',
                gender=CustomUser.GenderChoices.MALE.value,
                first_name='Abraham',
                last_name='Lincoln',
                father_name='Henry Morgan',
                date_of_birth=created_time_1,
                address='The Gettysburg Address',
                description='...'
            ),

            CustomUser(
                role=CustomUser.RoleChoices.PARENT.value,
                phone_number='+998999630099',
                email='parent2@dd.com',
                gender=CustomUser.GenderChoices.FEMALE.value,
                first_name='Margaret',
                last_name='Margareta',
                father_name='Luffy Margaret',
                date_of_birth=created_time_2,
                address='The Gettysburg 18 Address',
                description='...'
            ),

            CustomUser(
                role=CustomUser.RoleChoices.PARENT.value,
                phone_number='+998999657844',
                email='parent3@dd.com',
                gender=CustomUser.GenderChoices.MALE.value,
                first_name='Lory',
                last_name='Shenma',
                father_name='Alex Sen',
                date_of_birth=created_time_3,
                address='The USA street Address',
                description='...'
            ),

            CustomUser(
                role=CustomUser.RoleChoices.TEACHER.value,
                phone_number='+998904561263',
                email='teacher1@dd.com',
                gender=CustomUser.GenderChoices.FEMALE.value,
                first_name='Edna',
                last_name='Francis',
                father_name='Edward S.',
                date_of_birth=created_time_1,
                address='205 South Water Street North_field,',
                description='...'
            ),

            CustomUser(
                role=CustomUser.RoleChoices.TEACHER.value,
                phone_number='+998904563377',
                email='teacher2@dd.com',
                gender=CustomUser.GenderChoices.MALE.value,
                first_name='Holy',
                last_name='Ishra',
                father_name='Gvenra Ashra.',
                date_of_birth=created_time_2,
                address='205 South river Street South_field',
                description='...'
            ),

            CustomUser(
                role=CustomUser.RoleChoices.TEACHER.value,
                phone_number='+998904567788',
                email='teacher3@dd.com',
                gender=CustomUser.GenderChoices.FEMALE.value,
                first_name='Miya',
                last_name='Yutaro',
                father_name='Helmet Power',
                date_of_birth=created_time_3,
                address='302 North river Street North_field,',
                description='...'
            ),

            CustomUser(
                role=CustomUser.RoleChoices.STUDENT.value,
                phone_number='+998978526341',
                email='student1@dd.com',
                gender=CustomUser.GenderChoices.MALE.value,
                first_name='Robert',
                last_name='Hooke',
                father_name='Edward S.',
                date_of_birth=created_time_1,
                address=' Isle of Wight',
                description='...'
            ),

            CustomUser(
                role=CustomUser.RoleChoices.STUDENT.value,
                phone_number='+998970001200',
                email='student2@dd.com',
                gender=CustomUser.GenderChoices.MALE.value,
                first_name='Holy',
                last_name='Ednan',
                father_name='Stuart Hebinson.',
                date_of_birth=created_time_2,
                address=' island of Gimitery',
                description='...'
            ),

            CustomUser(
                role=CustomUser.RoleChoices.STUDENT.value,
                phone_number='+998978529988',
                email='student3@dd.com',
                gender=CustomUser.GenderChoices.FEMALE.value,
                first_name='Alex',
                last_name='Hoko',
                father_name='Albert Carlayel.',
                date_of_birth=created_time_3,
                address='London of 13 Wole Street',
                description='...'
            ),
        ]
        CustomUser.objects.bulk_create(users)
        self.stdout.write(self.style.SUCCESS(f'{len(users)} users were created.'))
