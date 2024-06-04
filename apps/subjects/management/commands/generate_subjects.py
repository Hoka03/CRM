from django.core.management import BaseCommand
from django.utils import timezone

from apps.subjects.models import Subject


class Command(BaseCommand):
    def handle(self, *args, **options):
        created_time_1 = timezone.datetime(1920, 5, 15, 10, 30, 0)
        created_time_2 = timezone.datetime(1860, 4, 20, 12, 45, 3)
        created_time_3 = timezone.datetime(1900, 8, 18, 15, 42, 8)

        subjects = [
            Subject(
                name='History',
                slug='history',
                price='360000',
                description='History is the study of change over time, ''and it covers all aspects of human'
                            ' society. Political, social, economic, scientific, ''technological, medical,'
                            ' cultural, intellectual, religious and military developments'
                            ' are all part of history',
                created_at=created_time_1),

            Subject(
                name='Physics',
                slug='physics',
                price='220000',
                description='Physics is the most basic of the sciences, concerning itself with energy, '
                            'matter, space and time, and their interactions. Scientific laws and theories express'
                            ' the general truths of nature and the body of knowledge they encompass',
                created_at=created_time_2,
            ),

            Subject(
                name='Philosophy',
                slug='philosophy',
                price='450000',
                description='Quite literally, the term "philosophy" means, "love of wisdom." In a broad sense, '
                            'philosophy is an activity people undertake when they seek to understand fundamental '
                            'truths about themselves, the world in which they live, and their relationships '
                            'to the world and to each other.',
                created_at=created_time_3
            ),
        ]
        Subject.objects.bulk_create(subjects)
        self.stdout.write(self.style.SUCCESS(f"{Subject.objects.count()}-subjects was created."))
