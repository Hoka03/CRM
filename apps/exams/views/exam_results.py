from django.shortcuts import redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, UpdateView, DeleteView
from django.urls import reverse_lazy

from apps.exams.models import ExamResult, Exam
from apps.users.models import CustomUser


class ExamGradesListView(ListView):
    template_name = 'exams/exam-grade.html'
    context_object_name = 'exam_results'

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['exams'] = Exam.objects.all().order_by('-id')
        context['students'] = get_user_model().objects.filter(role=CustomUser.RoleChoices.STUDENT.value)
        return context

    def get_queryset(self):
        queryset = ExamResult.objects.all()
        search_name = self.request.GET.get('search_name')
        if search_name:
            queryset = queryset.filter(exam__subject__name__icontains=search_name)

        search_percent = self.request.GET.get('search_percent')
        if search_percent:
            queryset = queryset.filter(percent__icontains=search_percent)
        return queryset

    def post(self, request):
        exam_id = request.POST.get('exam_id')
        student_id = request.POST.get('student_id')
        grade_point = request.POST.get('grade_point')
        percentage = request.POST.get('percentage')
        comment = request.POST.get('comment')

        ExamResult.objects.create(
            exam_id=exam_id,
            student_id=student_id,
            grade_point=grade_point,
            percent=percentage,
            comment=comment
        )
        return redirect('exam_grade')


class ExamResultDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = ExamResult
    template_name = 'exams/exam_delete.html'
    permission_required = ('users.delete_customuser')
    success_url = reverse_lazy('exam_grade')
