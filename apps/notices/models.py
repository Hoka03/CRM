from django.db import models

from apps.users.models import CustomUser
from apps.general.services import normalize_text


class Notification(models.Model):
    user_admin = models.ForeignKey(CustomUser, limit_choices_to={'role': CustomUser.RoleChoices.ADMIN.value},
                             on_delete=models.PROTECT)
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150)
    details = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user_admin}'


class Message(models.Model):
    from_user = models.ForeignKey(CustomUser, on_delete=models.PROTECT, related_name='from_user')
    to_user = models.ForeignKey(CustomUser, on_delete=models.PROTECT, related_name='to_user')
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150)
    message = models.TextField(max_length=2000)

    def __str__(self):
        return f'{self.from_user}: {self.to_user}'

    @classmethod
    def get_normalize_fields(cls):
        return ['title', 'slug', 'message']

    def save(self, *args, **kwargs):
        normalize_text(self)
        super().save(*args, **kwargs)
