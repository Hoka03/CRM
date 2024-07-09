from django.urls import path

from .views import LessonListView, LessonEditView


urlpatterns = [
    path('lesson/', LessonListView.as_view(), name='lesson_page'),
    path('lesson-edit/<int:pk>/', LessonEditView.as_view(), name='lesson_edit'),
]