from django import template

from apps.groups.models import StudentGroup

register = template.Library()


@register.filter
def normalize_month(moth):
    moths = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
             'November', 'December']
    if not moth.isdigit():
        return None
    if int(moth) > 12 or int(moth) < 1:
        return None
    return moths[int(moth)-1]


@register.filter
def get_student_id(group_id):
    if not group_id.isdigit():
        return None
    group = StudentGroup.objects.get(id=group_id)
    if not group:
        return None
    return group