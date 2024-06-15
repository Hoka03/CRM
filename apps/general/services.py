import os

from django.db.models import FileField, ImageField, CharField, TextField


def normalize_text(obj):
    for field in obj._meta.get_fields():
        if isinstance(field, (CharField, TextField)):
            obj_field = getattr(obj, field.name)
            setattr(obj, field.name, ' '.join(obj_field.split()))


def delete_file_after_delete_obj(instance):
    for field in instance._meta.get_fields():
        if isinstance(field, (FileField, ImageField)):
            field = getattr(instance, field.name, None)
            if field and os.path.isfile(field.path):
                os.remove(field.path)