from django.shortcuts import render

from django.views.generic import TemplateView


class MessageTemplateView(TemplateView):
    template_name = 'messaging.html'


class NoticeTemplateView(TemplateView):
    template_name = 'notice-board.html'