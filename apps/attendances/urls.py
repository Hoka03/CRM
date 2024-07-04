from django.urls import path

from .views import AttendanceTemplateView


urlpatterns = [
    path('attendance/', AttendanceTemplateView.as_view(), name='attendance_page')
]