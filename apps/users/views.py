from django.shortcuts import redirect
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth import logout, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DetailView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView, TemplateView

from .models import CustomUser
from .forms import AddStudentForm


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


class StudentDetailView(DetailView):
    template_name = 'student-details.html'
    # queryset = CustomUser.objects.filter(role=CustomUser.RoleChoices.STUDENT.value)
    # context_object_name = 'students'


class AccountTemplateView(TemplateView):
    template_name = 'account-settings.html'


# <====================== Parent Page ===================>

class ParentTemplateView(TemplateView):
    template_name = 'all-parents.html'


class ParentDetailTemplateView(TemplateView):
    template_name = 'parents-details.html'


class AddParentTemplateView(TemplateView):
    template_name = 'add-parents.html'


# <====================== Teacher Page ===================>

class TeacherTemplateView(TemplateView):
    template_name = 'all-teacher.html'


class TeacherDetailView(TemplateView):
    template_name = 'teacher-details.html'


class AddTeacherTemplateView(TemplateView):
    template_name = 'add-teacher.html'


class TeacherPaymentTemplateView(TemplateView):
    template_name = 'teacher-payment.html'


# <====================== Student Page ===================>
class StudentTemplateView(TemplateView):
    template_name = 'all-student.html'


class StudentPromotionTemplateView(TemplateView):
    template_name = 'student-promotion.html'


# <====================== Dashboard Page ===================>

class AdminDashboardTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'


class StudentDashboardTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'index3.html'


class ParentDashboardTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'index4.html'


class TeacherDashboardTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'index5.html'


class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name='admins').exists() and \
            self.request.user.has_perm('apps.users.view_CustomUser') and \
            self.request.user.has_perm('apps.users.add_CustomUser') and \
            self.request.user.has_perm('apps.users.add_CustomUser') and \
            self.request.user.has_perm('apps.users.change_CustomUser') and \
            self.request.user.has_perm('apps.users.delete_CustomUser')


class StudentRegisterView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = CustomUser
    fields = ['first_name', 'last_name', 'father_name', 'mother_name', 'date_of_birth', 'email', 'phone_number',
              'password', 'student_group', 'address', 'gender', 'photo']

    template_name = 'admit-form.html'

    permission_required = ('users.add_customuser')

    success_url = reverse_lazy('student_page')

    def form_valid(self, form):
        form.instance.role = CustomUser.RoleChoices.STUDENT
        return super().form_valid(form)

