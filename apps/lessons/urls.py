from django.urls import path

from .views import LessonListView


urlpatterns = [
    path('lesson/', LessonListView.as_view(), name='lesson_page')
]