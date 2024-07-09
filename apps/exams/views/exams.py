from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, UpdateView, DeleteView
from django.urls import reverse_lazy

from apps.exams.models import Exam, ExamResult
from apps.subjects.models import Subject


class ExamScheduleListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = 'exams/exam-schedule.html'
    context_object_name = 'exams'
    permission_required = ('users.create_customuser',)

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['subjects'] = Subject.objects.all().order_by('-id')
        exams = Exam.objects.all().order_by('-id')
        context['exams'] = exams
        context['exam_results'] = {exam.id: ExamResult.objects.filter(exam=exam).exists() for exam in exams}
        return context

    def get_queryset(self):
        queryset = Exam.objects.all()
        search_id = self.request.GET.get('search_id')
        if search_id:
            queryset = queryset.filter(id__startswith=search_id)

        search_name = self.request.GET.get('search_name')
        if search_name:
            queryset = queryset.filter(subject__name__icontains=search_name)
        return queryset

    def post(self, request):
        subject_id = request.POST.get('subject_id')
        select_time = request.POST.get('select_time')
        nth_month = request.POST.get('nth_month')
        day = request.POST.get('day')

        Exam.objects.create(
            subject_id=subject_id,
            limit_hour=select_time,
            nth_month=nth_month,
            created_at=day
        )
        return redirect('exam_schedule')


class ExamEditView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Exam
    fields = ['subject', 'nth_month', 'limit_hour']
    template_name = 'exams/exam_edit.html'
    permission_required = ('users.change_customuser')
    success_url = reverse_lazy('exam_schedule')


class ExamDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Exam
    template_name = 'exams/exam_delete.html'
    permission_required = ('users.delete_customuser',)
    success_url = reverse_lazy('exam_schedule')