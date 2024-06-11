from django.shortcuts import render
from django.views.generic import TemplateView


class GroupTemplateView(TemplateView):
    template_name = 'all-class.html'


class AddGroupTemplateView(TemplateView):
    template_name = 'add-class.html'
