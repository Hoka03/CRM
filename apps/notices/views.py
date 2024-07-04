from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.contrib import messages

from .models import Chat, ChatMessage
from .form import ChatMessageForm


class ChatListView(LoginRequiredMixin, ListView):
    queryset = Chat.objects.all()
    context_object_name = 'chats'
    template_name = 'chat/message.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        chat_id = self.request.GET.get('chat_id')
        if chat_id:
            # context['chat'] = Chat.objects.get(id=chat_id)
            context['chat_messages'] = ChatMessage.objects.filter(
                chat_id=chat_id).select_related('chat').order_by('is_viewed', '-created_at')
        else:
            # context['chat'] = None
            context['chat_messages'] = None
        return context

    def get_queryset(self):
        user = self.request.user
        self.queryset = self.queryset.filter(Q(recipient_id=user.id) | Q(sender_id=user.id)
                                        ).select_related('sender', 'recipient').prefetch_related('messages')

        search_name = self.request.GET.get('search_name')
        if search_name:
            self.queryset = self.queryset.filter(Q(sender__first_name__icontains=search_name) |
                                       Q(sender__last_name__icontains=search_name) |
                                       Q(recipient__first_name__icontains=search_name) |
                                       Q(recipient__last_name__icontains=search_name))

        return self.queryset

    def post(self, request, *args, **kwargs):
        chat_id = request.GET.get('chat_id')
        message = request.POST.get('message')
        if chat_id and message:
            form = ChatMessageForm({'chat': int(chat_id), 'message': message,
                                    'sender': request.user.pk})
            if form.is_valid():
                form.save()
            else:
                messages.error(request, 'Form Invalid  Data')
        else:
            message.error(request, 'Invalid request')
        return


# class CHatMessageListView(ListView):
#     model = ChatMessage
#     template_name = 'chat/message.html'
#     context_object_name = 'messages'
#
#     def get_queryset(self):
#         chat_id = self.request.GET.get('chat_id')
#         user = self.request.user
#         if chat_id:
#             return ChatMessage.objects.filter(chat_id=chat_id).order_by('is_viewed', '-created_at')
#         return ChatMessage.objects.none()
#
#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args, **kwargs)
#         chat_id = self.request.GET.get('chat_id')
#         context['chat'] = None
#         if chat_id:
#             try:
#                 context['chat'] = Chat.objects.get(id=chat_id)
#             except Chat.DoesNotExist:
#                 context['chat'] = None
#         return redirect('message_page')


class NoticeTemplateView(TemplateView):
    template_name = 'notice-board.html'
