from django.shortcuts import redirect, render
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
            context['chat_messages'] = ChatMessage.objects.filter(
                chat_id=chat_id).select_related('chat').order_by('is_viewed', 'created_at')
        else:
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

    def get(self, request, *args, **kwargs):
        context = {
            'chats': self.get_queryset(),
            'form': ChatMessageForm(),
            'chat_messages': ChatMessage.objects.filter(chat_id=request.GET.get('chat_id'))
        }
        return render(request, self.template_name, context)

    def post(self, request):
        chat_id = request.GET.get('chat_id')
        message = request.POST.get('message')
        image = request.FILES.get('image')
        if chat_id and (message or image):
            form_data = {'chat': chat_id, 'message': message,
                         'sender': request.user.id}
            form = ChatMessageForm(form_data, request.FILES)
            if form.is_valid():
                form.save()
            else:
                messages.error(request, 'Form Invalid  Data')
        else:
            messages.error(request, 'Missing chat_id or message.')
        return redirect(request.META['HTTP_REFERER'])


class NoticeTemplateView(TemplateView):
    template_name = 'notice-board.html'
