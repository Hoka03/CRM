from django.views.generic import TemplateView


class SubjectTemplateView(TemplateView):
    template_name = 'all-subject.html'


class BookTemplateView(TemplateView):
    template_name = 'all-book.html'


class AddBookTemplateView(TemplateView):
    template_name = 'add-book.html'