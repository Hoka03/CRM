from django.shortcuts import render

from django.views.generic import TemplateView


class AttendanceTemplateView(TemplateView):
    template_name = 'students/student-attendence.html'