from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.contrib.auth.views import LoginView, LogoutView, TemplateView

from .models import CustomUser


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


class ParentTemplateView(TemplateView):
    template_name = 'all-parents.html'


class ParentDetailTemplateView(TemplateView):
    template_name = 'parents-details.html'


class AddParentTemplateView(TemplateView):
    template_name = 'add-parents.html'


class TeacherTemplateView(TemplateView):
    template_name = 'all-teacher.html'


class TeacherDetailView(TemplateView):
    template_name = 'teacher-details.html'


class AddTeacherTemplateView(TemplateView):
    template_name = 'add-teacher.html'


class TeacherPaymentTemplateView(TemplateView):
    template_name = 'teacher-payment.html'


class StudentTemplateView(TemplateView):
    template_name = 'all-student.html'


class AddStudentTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'admit-form.html'


class StudentPromotionTemplateView(TemplateView):
    template_name = 'student-promotion.html'