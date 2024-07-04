from django import forms
from apps.notices.models import ChatMessage


class ChatMessageForm(forms.ModelForm):
    class Meta:
        model = ChatMessage
        fields = ['chat', 'sender', 'message']