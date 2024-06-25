from django.core.management import BaseCommand
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from config.settings import permissions


class Command(BaseCommand):
    def handle(self, *args, **options):
        student_group_permissions = Permission.objects.filter(codename__in=permissions.STUDENT_GROUP_PERMISSIONS)
        student_group = Group.objects.create(name='student')
        student_group.permissions.set(student_group_permissions)

        teacher_group_permissions = Permission.objects.filter(codename__in=permissions.TEACHER_GROUP_PERMISSIONS)
        teacher_group = Group.objects.create(name='teacher')
        teacher_group.permissions.set(teacher_group_permissions)

        parent_group_permissions = Permission.objects.filter(codename__in=permissions.PARENT_GROUP_PERMISSIONS)
        parent_group = Group.objects.create(name='parent')
        parent_group.permissions.set(parent_group_permissions)

        admin_group = Group.objects.create(name='admin')
        admin_group.permissions.set(Permission.objects.all())

        self.stdout.write(self.style.SUCCESS(f"{Group.objects.count()}-groups created."))