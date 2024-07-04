from django.urls import path

from .views import exams, exam_results

urlpatterns = [
    path('exam-schedule', exams.ExamScheduleListView.as_view(), name='exam_schedule'),
    path('exam-edit/<int:pk>/', exams.ExamEditView.as_view(), name='exam_edit'),
    path('exam-delete/<int:pk>/', exams.ExamDeleteView.as_view(), name='exam_delete'),
    path('exam-grade', exam_results.ExamGradesListView.as_view(), name='exam_grade'),
    path('exam-result-delete/<int:pk>/', exam_results.ExamResultDeleteView.as_view(), name='exam_result_delete')
]