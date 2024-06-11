from django.urls import path

from .views import MessageTemplateView, NoticeTemplateView


urlpatterns = [
    path('message-page/', MessageTemplateView.as_view(), name='message_page'),
    path('notice-page/', NoticeTemplateView.as_view(), name='notice_page')
]