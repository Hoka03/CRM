from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q

from .models import Resource, Subject


class SubjectTemplateView(ListView):

    template_name = 'all-subject.html'

    context_object_name = 'subjects'

    def get_queryset(self):
        queryset = Subject.objects.all()
        query = self.request.GET.get('q')

        if query:
            queryset = queryset.filter(
                Q(name__icontains=query) |
                Q(created_at__icontains=query)
            )
        return queryset


class BookTemplateView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Resource

    template_name = 'all-book.html'

    context_object_name = 'book'

    permission_required = ('users.view_customuser',)


class AddBookTemplateView(TemplateView):
    template_name = 'add-book.html'