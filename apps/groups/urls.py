from django.urls import path

from .views import GroupTemplateView, AddGroupView


urlpatterns = [
    path('all-class/', GroupTemplateView.as_view(), name='group_page'),
    path('add-class/', AddGroupView.as_view(), name='add_group_page')
]