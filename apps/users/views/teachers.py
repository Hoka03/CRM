from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import CreateView, DetailView, DeleteView, ListView, UpdateView, TemplateView
from django.urls import reverse_lazy
from django.db.models import Q

from apps.users.models import CustomUser


class TeacherTemplateView(ListView):
    template_name = 'teachers/all-teacher.html'
    context_object_name = 'teachers'

    def get_queryset(self):
        queryset = CustomUser.objects.filter(role=get_user_model().RoleChoices.TEACHER.value)
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(id__icontains=query) |
                Q(first_name__icontains=query) |
                Q(phone_number__icontains=query)
            )
        return queryset


class TeacherDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'teachers/teacher-details.html'
    context_object_name = 'teacher'
    permission_required = ('users.view_customuser',)


class TeacherPaymentTemplateView(TemplateView):
    template_name = 'teachers/teacher-payment.html'


class TeacherDashboardTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'index5.html'


class TeacherRegisterView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    ''' =============================== Add teachers ========================================== '''
    model = CustomUser
    fields = ['first_name', 'last_name', 'student_group', 'date_of_birth', 'email', 'phone_number',
              'password', 'address', 'gender', 'salary', 'photo']

    template_name = 'teachers/add-teacher.html'

    permission_required = ('users.add_customuser',)

    success_url = reverse_lazy('teacher_page')

    def form_valid(self, form):
        form.instance.role = CustomUser.RoleChoices.TEACHER
        return super().form_valid(form)


class TeacherDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = CustomUser

    template_name = 'delete_users/delete_teacher.html'

    permission_required = ('users.delete_customuser',)

    success_url = reverse_lazy('teacher_page')


class TeacherEditView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = CustomUser

    fields = ['first_name', 'last_name', 'student_group', 'date_of_birth', 'email', 'phone_number',
              'password', 'address', 'gender', 'salary', 'photo']

    template_name = 'edit_users/teacher_edit.html'

    permission_required = ('users.change_customuser',)

    success_url = reverse_lazy('teacher_page')