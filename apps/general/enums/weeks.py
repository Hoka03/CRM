from django.db import models


class WeekDay(models.IntegerChoices):
    MONDAY = 0, 'monday'
    TUESDAY = 1, 'tuesday'
    WEDNESDAY = 2, 'wednesday'
    THURSDAY = 3, 'thursday'
    FRIDAY = 4, 'friday'
    SATURDAY = 5, 'saturday'
    SUNDAY = 6, 'sunday'