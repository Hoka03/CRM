from django.urls import path

from .views import ExamScheduleTemplateView, ExamGradesTemplateView


urlpatterns = [
    path('exam-schedule', ExamScheduleTemplateView.as_view(), name='exam_schedule'),
    path('exam-grade', ExamGradesTemplateView.as_view(), name='exam_grade')
]