from django.views.generic import ListView
from django.db.models import Q

from .models import Lesson


class LessonListView(ListView):
    model = Lesson

    template_name = 'all-lessons.html'

    context_object_name = 'lessons'

    def get_queryset(self):
        queryset = Lesson.objects.all()
        query = self.request.GET.get('q')

        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) |
                Q(ordering_number__icontains=query)
            )

        return queryset