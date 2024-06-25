from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from .models import Resource, Subject


class SubjectListView(ListView):

    template_name = 'all-subject.html'

    context_object_name = 'subjects'

    def get_queryset(self):
        queryset = Subject.objects.all()

        search_id = self.request.GET.get('search_id')
        if search_id:
            queryset = queryset.filter(id__startswith=search_id)

        search_name = self.request.GET.get('search_name')
        if search_name:
            queryset = queryset.filter(name=search_name)

        return queryset


class BookListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Resource

    template_name = 'all-book.html'

    context_object_name = 'book'

    permission_required = ('users.view_customuser',)


class AddBookTemplateView(TemplateView):
    template_name = 'add-book.html'