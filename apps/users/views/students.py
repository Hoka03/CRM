from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import CreateView, DetailView, DeleteView, ListView, UpdateView, TemplateView
from django.urls import reverse_lazy
from django.db.models import Q

from apps.users.models import CustomUser


class StudentTemplateView(ListView):
    template_name = 'students/all-student.html'
    context_object_name = 'students'

    def get_queryset(self):
        queryset = CustomUser.objects.filter(role=get_user_model().RoleChoices.STUDENT.value)
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(id__icontains=query) |
                Q(first_name__icontains=query) |
                Q(phone_number__icontains=query)
            )
        return queryset


class StudentDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'students/student-details.html'
    context_object_name = 'student'
    permission_required = ('users.view_student',)


class StudentPromotionTemplateView(TemplateView):
    template_name = 'students/student-promotion.html'


class StudentDashboardTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'index3.html'


class StudentRegisterView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    ''' =============================== Add students ========================================== '''
    model = CustomUser
    fields = ['first_name', 'last_name', 'father_name', 'mother_name', 'date_of_birth', 'email', 'phone_number',
              'password', 'student_group', 'address', 'gender', 'photo']

    template_name = 'students/admit-form.html'

    permission_required = ('users.view_subject', 'users.view_exam', 'users.view_payment')

    success_url = reverse_lazy('student_page')

    def form_valid(self, form):
        form.instance.role = CustomUser.RoleChoices.STUDENT
        return super().form_valid(form)


class StudentDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = CustomUser

    template_name = 'delete_users/student_delete.html'

    permission_required = ('users.delete_customuser',)

    success_url = reverse_lazy('student_page')


class StudentEditView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = CustomUser
    fields = ['first_name', 'last_name', 'father_name', 'mother_name', 'date_of_birth', 'email', 'phone_number',
              'password', 'student_group', 'address', 'gender', 'photo']

    template_name = 'edit_users/student_edit.html'

    permission_required = ('users.change_customuser',)

    success_url = reverse_lazy('student_page')
