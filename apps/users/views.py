from django.shortcuts import redirect
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth import logout, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import CreateView, DetailView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView, TemplateView

from .models import CustomUser


# <=================== Login  Logout ===============>
class UserLoginView(LoginView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().get(request, *args, **kwargs)


class UserLogoutView(LoginRequiredMixin, LogoutView):
    http_method_names = ['post', 'get']

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)


class StudentDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'students/student-details.html'
    context_object_name = 'student'
    permission_required = ('users.view_student',)



class AccountTemplateView(TemplateView):
    template_name = 'account-settings.html'


# <====================== Parent Page ===================>

class ParentTemplateView(TemplateView):
    template_name = 'parents/all-parents.html'


class ParentDetailTemplateView(TemplateView):
    template_name = 'parents/parents-details.html'


# <====================== Teacher Page ===================>

class TeacherTemplateView(TemplateView):
    template_name = 'all-teacher.html'


class TeacherDetailView(TemplateView):
    template_name = 'teachers/teacher-details.html'


class TeacherPaymentTemplateView(TemplateView):
    template_name = 'teachers/teacher-payment.html'


# <====================== Student Page ===================>
class StudentTemplateView(ListView):
    template_name = 'students/all-student.html'
    context_object_name = 'students'
    queryset = CustomUser.objects.filter(role=get_user_model().RoleChoices.STUDENT)


class StudentPromotionTemplateView(TemplateView):
    template_name = 'students/student-promotion.html'


# <====================== Dashboard Page ===================>

class AdminDashboardTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'


class StudentDashboardTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'index3.html'


class ParentDashboardTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'index4.html'


class TeacherDashboardTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'index5.html'


# <========================== Add Users ===============================>


class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name='admins').exists() and \
            self.request.user.has_perm('apps.users.view_CustomUser') and \
            self.request.user.has_perm('apps.users.add_CustomUser') and \
            self.request.user.has_perm('apps.users.add_CustomUser') and \
            self.request.user.has_perm('apps.users.change_CustomUser') and \
            self.request.user.has_perm('apps.users.delete_CustomUser')


class StudentRegisterView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = CustomUser
    fields = ['first_name', 'last_name', 'father_name', 'mother_name', 'date_of_birth', 'email', 'phone_number',
              'password', 'student_group', 'address', 'gender', 'photo']

    template_name = 'students/admit-form.html'

    permission_required = ('users.add_customuser')

    success_url = reverse_lazy('student_page')

    def form_valid(self, form):
        form.instance.role = CustomUser.RoleChoices.STUDENT
        return super().form_valid(form)


class TeacherRegisterView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = CustomUser
    fields = ['first_name', 'last_name', 'date_of_birth', 'email', 'phone_number',
              'password', 'address', 'gender', 'salary', 'photo']

    template_name = 'teachers/add-teacher.html'

    permission_required = ('users.add_customuser')

    success_url = reverse_lazy('teacher_page')

    def form_valid(self, form):
        form.instance.role = CustomUser.RoleChoices.TEACHER
        return super().form_valid(form)


class ParentRegisterView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = CustomUser
    fields = ['first_name', 'last_name', 'date_of_birth', 'email', 'phone_number', 'password', 'address', 'gender',
              'child', 'photo',]

    template_name = 'parents/add-parents.html'

    permission_required = ('users.add_customuser')

    success_url = reverse_lazy('parent_page')

    def form_valid(self, form):
        form.instance.role = CustomUser.RoleChoices.PARENT
        return super().form_valid(form)


# <================================== Delete Users ================================>


class StudentDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = CustomUser

    template_name = 'delete_users/confirm_delete.html'

    permission_required = ('users.delete_customuser')

    success_url = reverse_lazy('student_page')


# <================================= Edit Users ===================================>


class StudentEditView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = CustomUser
    fields = ['first_name', 'last_name', 'father_name', 'mother_name', 'date_of_birth', 'email', 'phone_number',
              'password', 'student_group', 'address', 'gender', 'photo']

    template_name = 'edit_users/confirm_edit.html'

    permission_required = ('users.change_customuser')

    success_url = reverse_lazy('student_page')