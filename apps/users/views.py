from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.contrib.auth.views import LoginView, LogoutView, TemplateView

from .models import CustomUser


class HomeTemplateView(TemplateView):
    template_name = 'index.html'


class UserLoginView(LoginView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().get(request, *args, **kwargs)


class UserLogoutView(LoginRequiredMixin, LogoutView):
    http_method_names = ['post', 'get']


class StudentDetailView(DetailView):
    template_name = 'student-details.html'
    queryset = CustomUser.objects.filter(role=CustomUser.RoleChoices.STUDENT.value)
    context_object_name = 'students'


# class LoginView(FormView):
#     form_class = LoginForm
#     template_name = 'login.html'
#     success_url = reverse_lazy(settings.LOGIN_REDIRECT_URL)
#
#     def form_valid(self, form):
#         data = form.cleaned_data
#         user = authenticate(self.request, username=data['username'], password=data['password'])
#         if user is not None:
#             login(self.request, user)
#         else:
#             messages.error(self.request, 'User does not exist')
#             return redirect('login')
#         return super().form_valid(form)

