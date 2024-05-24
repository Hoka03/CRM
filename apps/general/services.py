from django.utils.translation import get_language


def normalize_text(obj):
    for i in obj.get_normalize_fields():
        fields = getattr(obj, i)
        setattr(obj, i, ' '.join(fields.split()))


def get_field_by_language(obj, field_name):
    return getattr(obj, f'{field_name}_{get_language()}', field_name)