from django.core.management import BaseCommand
from django.utils import timezone

from apps.groups.models import StudentGroup
from apps.general.enums.weeks import WeekDay
from apps.users.models import CustomUser
from apps.subjects.models import Subject


class Command(BaseCommand):
    def handle(self, *args, **options):
        teacher = CustomUser.objects.get(first_name='Edna')
        # second_teacher = CustomUser.objects.get(first_name='Holy')
        # third_teacher = CustomUser.objects.get(first_name='Miya')

        created_time_1 = timezone.datetime(2024, 2, 10, 6, 45, 0)
        created_time_2 = timezone.datetime(2024, 4, 18, 8, 10, 10)
        created_time_3 = timezone.datetime(2024, 6, 26, 10, 4, 20)
        student_groups = [

            StudentGroup(
                teacher_id=teacher.id,
                subject_id=Subject.objects.get(name="History").id,
                start_time=created_time_1.time(),
                end_time=(created_time_1 + timezone.timedelta(hours=1, minutes=20)).time(),
                week_day=[WeekDay.MONDAY.value],
                created_at=created_time_1
            ),

            StudentGroup(
                teacher_id=teacher.id,
                subject_id=Subject.objects.get(name="Physics").id,
                start_time=created_time_2.time(),
                end_time=(created_time_2 + timezone.timedelta(hours=1, minutes=20)).time(),
                week_day=[WeekDay.TUESDAY.value],
                created_at=created_time_2
            ),

            StudentGroup(
                teacher_id=teacher.id,
                subject_id=Subject.objects.get(name="Philosophy").id,
                start_time=created_time_3.time(),
                end_time=(created_time_3 + timezone.timedelta(hours=1, minutes=20)).time(),
                week_day=[WeekDay.WEDNESDAY.value],
                created_at=created_time_3
            ),
        ]
        StudentGroup.objects.bulk_create(student_groups)
        self.stdout.write(self.style.SUCCESS(f"{StudentGroup.objects.count()}-groups was created."))
