from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import CreateView, DetailView, DeleteView, ListView, UpdateView, TemplateView
from django.urls import reverse_lazy
from django.db.models import Q

from apps.users.models import CustomUser


class ParentTemplateView(ListView):
    template_name = 'parents/all-parents.html'
    context_object_name = 'parents'

    def get_queryset(self):
        queryset = CustomUser.objects.filter(role=get_user_model().RoleChoices.PARENT.value)
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(id__icontains=query) |
                Q(first_name__icontains=query) |
                q(phone_number__icontains=query)
            )
        return queryset


class ParentDetailTemplateView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'parents/parents-details.html'
    context_object_name = 'teacher'
    permission_required = ('users.view_student',)


class ParentDashboardTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'index4.html'


class ParentRegisterView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = CustomUser
    fields = ['first_name', 'last_name', 'date_of_birth', 'email', 'phone_number', 'password', 'address', 'gender',
              'child', 'photo',]

    template_name = 'parents/add-parents.html'

    permission_required = ('users.add_customuser',)

    success_url = reverse_lazy('parent_page')

    def form_valid(self, form):
        form.instance.role = CustomUser.RoleChoices.PARENT
        return super().form_valid(form)


class ParentDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = CustomUser

    template_name = 'delete_users/delete_parent.html'

    permission_required = ('users.delete_customuser',)

    success_url = reverse_lazy('parent_page')


class ParentEditView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = CustomUser

    fields = ['first_name', 'last_name', 'date_of_birth', 'email', 'phone_number', 'password', 'address', 'gender',
              'child', 'photo',]

    template_name = 'edit_users/parent_edit.html'

    permission_required = ('users.change_customuser',)

    success_url = reverse_lazy('parent_page')