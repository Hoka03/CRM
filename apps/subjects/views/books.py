from django.views.generic import TemplateView, ListView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy

from apps.subjects.models import Resource


class BookListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Resource
    template_name = 'books/all-book.html'

    context_object_name = 'books'

    permission_required = ('users.view_customuser',)

    def get_queryset(self):
        queryset = Resource.objects.all()
        search_id = self.request.GET.get('search_id')
        search_name = self.request.GET.get('search_name')

        if search_id:
            queryset = queryset.filter(id__startswith=search_id),

        if search_name:
            queryset = queryset.filter(book_name__icontains=search_name)

        return queryset


class BookEditView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Resource
    fields = ['book_name', 'subject', 'confirmed_by', 'published_at']
    template_name = 'books/all-book.html'
    permission_required = ('users.change_customuser')
    success_url = reverse_lazy('all_book_page')


class AddBookTemplateView(TemplateView):
    template_name = 'books/add-book.html'