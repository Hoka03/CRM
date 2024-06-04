from django.core.management import BaseCommand
from django.db import transaction
from apps.users.models import CustomUser
from django.db.models.deletion import ProtectedError


class Command(BaseCommand):
    def handle(self, *args, **options):
        usernames = ['abraham-lincoln', 'edna-francis', 'robert-hooke']

        for username in usernames:
            try:
                with transaction.atomic():
                    existing_user = CustomUser.objects.get(username=username)
                    existing_user.delete()
                    self.stdout.write(self.style.SUCCESS(f"User {username} deleted successfully."))
            except CustomUser.DoesNotExist:
                self.stdout.write(self.style.WARNING(f"User {username} not found."))
            except ProtectedError as e:
                self.stdout.write(self.style.ERROR(f"Cannot delete user {username}: {e}"))
