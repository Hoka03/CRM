import os
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save, post_init, pre_init, post_delete, pre_delete

from .models import CustomUser
from apps.general.services import normalize_text


@receiver(pre_save, sender=CustomUser)
def pre_save_user(instance, *args, **kwargs):
    print('WORKED!')
    normalize_text(instance)


@receiver(post_delete, sender=CustomUser)
def delete_photo_on_delete_user(instance, *args, **kwargs):
    os.remove(instance.photo.path)