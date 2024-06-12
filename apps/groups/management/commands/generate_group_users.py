from django.core.management import BaseCommand
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission


class Command(BaseCommand):
    def handle(self, *args, **options):
        student_group = Group.objects.create(name='student')
        student_group.permissions.set([92, 88, 96, 104, 108, 112, 116, 124, 120])

        teacher_group = Group.objects.create(name='teacher')
        teacher_group.permissions.set([120, 124, 118, 116, 112, 108, 104, 102, 100, 96, 93, 92, 89, 88, 85, ])

        parent_group = Group.objects.create(name='parent')
        parent_group.permissions.set([120, 116, 112, 108, 104, 100, 96, 88])

        admin_group = Group.objects.create(name='admin')
        admin_group.permissions.set(Permission.objects.all())

        self.stdout.write(self.style.SUCCESS(f"{Group.objects.count()}-groups created."))