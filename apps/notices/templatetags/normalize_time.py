from django import template
from django.utils.timezone import now

register = template.Library()


@register.filter
def date_time_to_minute(created_at):
    current_datetime = now() - created_at
    seconds = abs(int(current_datetime.total_seconds()))

    if seconds < 60:
        return f'{seconds} seconds'

    minutes = seconds // 60
    if minutes < 60:
        return f'{minutes} minutes'

    hours = minutes // 24
    if hours < 24:
        return f'{hours} hours'

    days = hours // 24
    if days < 7:
        return f'{days} days'

    weeks = days // 7
    return f'{weeks} weeks'