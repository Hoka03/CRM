from django.urls import path

from .views import ChatListView, NoticeTemplateView


urlpatterns = [
    path('message-page/', ChatListView.as_view(), name='message_page'),
    path('notice-page/', NoticeTemplateView.as_view(), name='notice_page')
]