from django.core.management import BaseCommand

from apps.exams.models import Exam
from apps.general.enums.months import MonthChoice
from apps.subjects.models import Subject


class Command(BaseCommand):
    def handle(self, *args, **options):
        exams = [
            Exam(
                subject_id=Subject.objects.get(name="History").id,
                nth_month=MonthChoice.February,
                limit_hour=2
            ),

            Exam(
                subject_id=Subject.objects.get(name="Physics").id,
                nth_month=MonthChoice.March,
                limit_hour=3
            ),

            Exam(
                subject_id=Subject.objects.get(name="Philosophy").id,
                nth_month=MonthChoice.April,
                limit_hour=2
            )
        ]
        Exam.objects.bulk_create(exams)
        self.stdout.write(self.style.SUCCESS(f"{Exam.objects.count()}-exams was created."))