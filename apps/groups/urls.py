from django.urls import path

from .views import GroupTemplateView, AddGroupView, GroupDeleteView, GroupEditView


urlpatterns = [
    path('all-class/', GroupTemplateView.as_view(), name='group_page'),
    path('add-class/', AddGroupView.as_view(), name='add_group_page'),
    path('delete-class/<int:pk>/', GroupDeleteView.as_view(), name='student_group_delete'),
    path('edit-class/<int:pk>/', GroupEditView.as_view(), name='student_group_edit'),
]