from django.shortcuts import redirect
from django.views.generic import ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy

from .models import Lesson
from apps.subjects.models import Subject


class LessonListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = 'lessons/all-lessons.html'
    context_object_name = 'lessons'
    permission_required = ('users.create_customuser',)

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['subjects'] = Subject.objects.all().order_by('-id')
        return context

    def get_queryset(self):
        queryset = Lesson.objects.all()

        search_name = self.request.GET.get('search_name')
        if search_name:
            queryset = queryset.filter(subject__name=search_name)

        search_ordering_number = self.request.GET.get('search_ordering_number')
        if search_ordering_number:
            queryset = queryset.filter(ordering_number=search_ordering_number)

        return queryset

    def post(self, request):
        subject_id = request.POST.get('subject_id')
        title = request.POST.get('title')
        content = request.POST.get('content')

        subject = Subject.objects.get(id=subject_id)

        Lesson.objects.create(
            subject=subject,
            title=title,
            content=content
        )
        return redirect('lesson_page')


class LessonEditView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Lesson
    template_name = 'lessons/edit-lesson.html'
    fields = ['subject', 'title', 'content']
    permission_required = ('users.change_customuser',)
    success_url = reverse_lazy('lesson_page')