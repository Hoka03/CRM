from django.urls import path

from .views import GroupTemplateView, AddGroupTemplateView


urlpatterns = [
    path('all-class/', GroupTemplateView.as_view(), name='group_page'),
    path('add-class/', AddGroupTemplateView.as_view(), name='add_group_page')
]