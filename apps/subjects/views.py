from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView, FormView

from apps.subjects.models import Subject
from .forms import SubjectForm


class SubjectListView(ListView):
    model = Subject


class SubjectFormView(FormView):
    template_name = 'subjects/subject_list.html'
    form_class = SubjectForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.save()
        # name = form.cleaned_data['name']
        # slug = form.cleaned_data['slug']
        # price = form.cleaned_data['price']
        # description = form.cleaned_data['description']
        # created_at = form.cleaned_data['created_at']

        return super().form_valid(form)