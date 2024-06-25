from django.views.generic import ListView

from .models import Lesson


class LessonListView(ListView):
    model = Lesson

    template_name = 'all-lessons.html'

    context_object_name = 'lessons'

    def get_queryset(self):
        queryset = Lesson.objects.all()

        search_name = self.request.GET.get('search_name')
        if search_name:
            queryset = queryset.filter(subject__name=search_name)

        search_ordering_number = self.request.GET.get('search_ordering_number')
        if search_ordering_number:
            queryset = queryset.filter(ordering_number=search_ordering_number)

        return queryset