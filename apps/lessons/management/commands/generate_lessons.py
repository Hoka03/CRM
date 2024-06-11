from django.core.management import BaseCommand

from apps.lessons.models import Lesson
from apps.subjects.models import Subject


class Command(BaseCommand):
    def handle(self, *args, **options):
        lessons = [
            Lesson(
                subject_id=Subject.objects.get(name="History").id,
                title='Historical development of the industrial revolution.',
                ordering_number=1,
                content='The Industrial Revolution transformed economies that had been based on agriculture'
                        'and handicrafts into economies based on large-scale industry, mechanized manufacturing,'
                        ' and the factory system. New machines, new power sources, and new ways of organizing work'
                        ' made existing industries more productive and efficient'
            ),

            Lesson(
                subject_id=Subject.objects.get(name="Physics").id,
                title='General relativity',
                ordering_number=2,
                content='General relativity, also known as the general theory of relativity and Einstein''s '
                        'theory of gravity, is the geometric theory of gravitation published by Albert Einstein '
                        'in 1915 and is the current description of gravitation in modern physics',
            ),

            Lesson(
                subject_id=Subject.objects.get(name="Philosophy").id,
                title='The Philosophy of Mind: Consciousness and Identity',
                ordering_number=3,
                content='The word consciousness is used in a variety of ways that need to be distinguished. Sometimes'
                        ' the word means merely any human mental activity at all (as when one talks about the “history'
                        ' of consciousness”), and sometimes it means merely being awake (as in As the anesthetic wore'
                        ' off, the animal regained consciousness)',
            ),
        ]
        Lesson.objects.bulk_create(lessons)
        self.stdout.write(self.style.SUCCESS(f"{Lesson.objects.count()}-lessons was created."))