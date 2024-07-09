from django.shortcuts import redirect
from django.views.generic import ListView, DeleteView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy

from apps.subjects.models import Resource, Subject
from apps.subjects.forms import ResourceForm


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
            queryset = queryset.filter(id__startswith=search_id)

        if search_name:
            queryset = queryset.filter(book_name__icontains=search_name)

        return queryset


class BookEditView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Resource
    fields = ['book_name', 'subject', 'confirmed_by', 'published_at']
    template_name = 'books/edit-book.html'
    permission_required = ('users.change_customuser',)
    success_url = reverse_lazy('all_book_page')


class BookDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Resource
    template_name = 'books/delete-book.html'
    permission_required = ('users.delete_customuser')
    success_url = reverse_lazy('all_book_page')


class AddBookTemplateView(CreateView):
    model = Resource
    template_name = 'books/add-book.html'
    form_class = ResourceForm

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['subjects'] = Subject.objects.all().order_by('-id')
        return context

    def post(self, request, *args, **kwargs):
        book_name = self.request.POST.get('book_name')
        subject_id = self.request.POST.get('subject_id')
        confirmed_by = self.request.POST.get('confirmed_by')
        published_at = self.request.POST.get('published_at')

        Resource.objects.create(
            book_name=book_name,
            subject_id=subject_id,
            confirmed_by=confirmed_by,
            published_at=published_at
        )
        return redirect('all_book_page')