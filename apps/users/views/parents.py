from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import CreateView, DetailView, DeleteView, ListView, UpdateView, TemplateView
from django.urls import reverse_lazy
from django.db.models import Q

from apps.users.models import CustomUser


class ParentListView(ListView):
    template_name = 'parents/all-parents.html'
    context_object_name = 'parents'

    def get_queryset(self):
        queryset = CustomUser.objects.filter(role=get_user_model().RoleChoices.PARENT.value)

        search_id = self.request.GET.get('search_id')
        if search_id:
            queryset = queryset.filter(id__startswith=search_id)

        search_name = self.request.GET.get('search_name')
        if search_name:
            queryset = queryset.filter(Q(first_name__icontains=search_name)
                                       |
                                       Q(last_name__icontains=search_name)
                                       |
                                       Q(father_name__icontains=search_name))

        search_phone_number = self.request.GET.get('search_phone_number')
        if search_phone_number:
            queryset = queryset.filter(phone_number=search_phone_number)

        return queryset


class ParentDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
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