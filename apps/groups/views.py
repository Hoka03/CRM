from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy

from apps.groups.models import StudentGroup
from apps.users.models import CustomUser
from apps.subjects.models import Subject
from .forms import AddGroupForm
from apps.general.enums.weeks import WeekDay


class GroupTemplateView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = 'classes/all-class.html'
    model = StudentGroup
    context_object_name = 'student_groups'
    permission_required = ('users.add_customuser')

    def get_queryset(self):
        queryset = StudentGroup.objects.all()
        search_id = self.request.POST.get('search_id')
        if search_id:
            queryset = queryset.filter(search_id__startswith=search_id)

        search_name = self.request.POST.get('search_name')
        if search_name:
            queryset = queryset.filter(student_group__teacher__first_name__icontains=search_name)

        search_class = self.request.POST.get('search_class')
        if search_class:
            queryset = queryset.filter(student_group__subject__icontains=search_class)
        return queryset


class AddGroupView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = StudentGroup
    form_class = AddGroupForm
    template_name = 'classes/add-class.html'
    permission_required = ('users.add_customuser')
    success_url = reverse_lazy('classes:all-class')
    context_object_name = 'groups'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teachers'] = CustomUser.objects.filter(role=CustomUser.RoleChoices.TEACHER.value)
        context['subjects'] = Subject.objects.all().order_by('-id')
        context['week_days'] = WeekDay.choices
        return context

    def post(self, request, *args, **kwargs):
        teacher_id = self.request.POST.get('teacher_id')
        subject_id = self.request.POST.get('subject_id')
        start_time = self.request.POST.get('start_time')
        end_time = self.request.POST.get('end_time')
        week_day = self.request.POST.get('week_day')

        teacher = CustomUser.objects.get(id=teacher_id)
        subject = Subject.objects.get(id=subject_id)

        week_day_array = '{' + ','.join(week_day) + '}'

        StudentGroup.objects.create(
            teacher=teacher,
            subject=subject,
            start_time=start_time,
            end_time=end_time,
            week_day=week_day_array
        )
        return redirect('group_page')


class GroupDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = StudentGroup
    template_name = 'classes/delete-class.html'
    permission_required = ('users.delete_customuser',)
    success_url = reverse_lazy('group_page')


class GroupEditView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = StudentGroup
    template_name = 'classes/edit-class.html'
    fields = ['teacher', 'subject', 'start_time', 'end_time']
    permission_required = ('users.change_customuser',)
    success_url = reverse_lazy('group_page')