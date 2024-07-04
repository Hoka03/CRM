import os

from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('makemigraitons'))
        os.system('python manage.py makemigrations')
        self.stdout.write(self.style.SUCCESS('migrate'))
        os.system('python manage.py migrate')
        self.stdout.write(self.style.SUCCESS('generate_students'))
        os.system('python manage.py generate_students')
        self.stdout.write(self.style.SUCCESS('generate_parents'))
        os.system('python manage.py generate_parents')
        self.stdout.write(self.style.SUCCESS('generate_teachers'))
        os.system('python manage.py generate_teachers')
        self.stdout.write(self.style.SUCCESS('generate_groups_users'))
        os.system('python manage.py generate_group_users')
        self.stdout.write(self.style.SUCCESS('generate_subjects'))
        os.system('python manage.py generate_subjects')
        self.stdout.write((self.style.SUCCESS('generate_lessons')))
        os.system('python manage.py generate_lessons')
        self.stdout.write(self.style.SUCCESS('generate_groups'))
        os.system('python manage.py generate_groups')
        self.stdout.write((self.style.SUCCESS('generate_exams')))
        os.system('python manage.py generate_exams')
        self.stdout.write((self.style.SUCCESS('generate_payments')))
        os.system('python manage.py generate_payments')


