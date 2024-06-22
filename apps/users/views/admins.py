from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout


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


class AdminDashboardTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'


class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name='admins').exists() and \
            self.request.user.has_perm('apps.users.view_CustomUser') and \
            self.request.user.has_perm('apps.users.add_CustomUser') and \
            self.request.user.has_perm('apps.users.add_CustomUser') and \
            self.request.user.has_perm('apps.users.change_CustomUser') and \
            self.request.user.has_perm('apps.users.delete_CustomUser')


class AccountTemplateView(TemplateView):
    template_name = 'account-settings.html'