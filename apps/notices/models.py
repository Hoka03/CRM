from django.db import models

from apps.users.models import CustomUser


class Notification(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    title = models.CharField(max_length=150)
    viewed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user