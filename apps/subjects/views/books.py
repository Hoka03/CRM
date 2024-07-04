from django.views.generic import TemplateView, ListView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy


from apps.subjects.models import Resource


class BookListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Resource

    template_name = 'all-book.html'

    context_object_name = 'book'

    permission_required = ('users.view_customuser',)


class AddBookTemplateView(TemplateView):
    template_name = 'add-book.html'