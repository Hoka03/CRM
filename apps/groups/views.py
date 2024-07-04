from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from apps.groups.models import StudentGroup


class GroupTemplateView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = 'classes/all-class.html'
    model = StudentGroup
    context_object_name = 'student_groups'
    permission_required = ('users.add_customuser')


class AddGroupTemplateView(TemplateView):
    template_name = 'classes/add-class.html'
