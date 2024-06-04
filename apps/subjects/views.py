from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, DeleteView, CreateView, FormView

from apps.subjects.models import Subject
from apps.lessons.models import Lesson


def home(request):
    lng = request.GET.get('language')
    ctx = {
        "salom": ['hello', 'world'],
        "lng": lng
    }
    return render(request, 'index.html', ctx)


# class HomeView(View):
#     def get(self, request):
#         return HttpResponse("hello")
#
#     def post(self, request):
#         return render(request, 'index.html')

class HomeTemplateView(TemplateView):
    template_name = "index.html"
    extra_context = {
        "salom": ['hello', 'world'],
        'subjects': Subject.objects.all()
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lng'] = self.request.GET.get('language')
        context['subjects_starting_with_a'] = Subject.objects.filter(name__icontains="History")
        return context


class SubjectListView(ListView):
    paginate_by = 2
    queryset = Subject.objects.order_by('-price')
    context_object_name = 'subject'
    extra_context = {
        'lessons': Lesson.objects.all()
    }

    def get_queryset(self):
        category_id = self.request.GET.get('category_id')
        return self.queryset.filter()


class SubjectDetailView(DetailView):
    model = Subject
