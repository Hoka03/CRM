import os

from django.db.models import FileField, ImageField, CharField, TextField


def normalize_text(obj):
    for field in obj._meta.get_fields():
        if isinstance(field, (CharField, TextField)):
            obj_field = getattr(obj, field.name)
            if isinstance(obj_field, str) and obj_field is not None:
                setattr(obj, field.name, ' '.join(obj_field.split()))


def delete_file_after_delete_obj(instance):
    for field in instance._meta.get_fields():
        if isinstance(field, (FileField, ImageField)):
            file_field = getattr(instance, field.name, None)
            if file_field and os.path.isfile(file_field.path):
                os.remove(file_field.path)
