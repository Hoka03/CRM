from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy

from apps.groups.models import StudentGroup
from .forms import AddGroupForm


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