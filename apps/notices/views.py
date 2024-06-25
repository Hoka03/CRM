from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

from .models import Message


class MessageTemplateView(LoginRequiredMixin, ListView):
    template_name = 'chat/message.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        chat_id = self.request.GET.get('chat_id')
        if chat_id:
            context['chat'] = Message.objects.get(id=chat_id)
        else:
            context['chat'] = None

        return context

    def get_queryset(self):
        user = self.request.user
        queryset = Message.objects.filter(Q(from_user_id=user.id) | Q(to_user_id=user.id)
                                          ).select_related('to_user', 'from_user'
                                                           ).order_by('is_viewed', '-created_at')

        search_name = self.request.GET.get('search_name')
        if search_name:
            queryset = queryset.filter(get_full_name=search_name)

        return queryset


class NoticeTemplateView(TemplateView):
    template_name = 'notice-board.html'
