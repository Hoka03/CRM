import os

from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('DATABASE WAS DELETED SUCCESSFULLY'))
        os.system('rm -rf db.sqlite3')
        self.stdout.write(self.style.SUCCESS('makemigraitons'))
        os.system('python manage.py makemigrations')
        self.stdout.write(self.style.SUCCESS('migrate'))
        os.system('python manage.py migrate')
        self.stdout.write(self.style.SUCCESS('generate_users'))
        os.system('python manage.py generasubjectste_users')
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
        self.stdout.write(self.style.SUCCESS('generate_groups_users'))
        os.system('python manage.py generate_group_users')

