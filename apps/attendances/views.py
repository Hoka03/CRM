import calendar
from datetime import date
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import redirect
from apps.users.models import CustomUser
from apps.groups.models import StudentGroup
from apps.attendances.models import Attendance
from django.http import HttpRequest, HttpResponse
from apps.attendances.forms import AttendanceCreateForm
from django.views.generic import TemplateView, CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class AttendanceTemplateView(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
    template_name = "students/student-attendance.html"
    context_object_name = 'attendances'
    permission_required = ('attendances.view_attendance',)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.role == 2:
            context['groups'] = list(StudentGroup.objects.filter(teacher_id=self.request.user.pk).select_related(
                'subject').order_by('subject__name').last()),
        else:
            context['groups'] = list(StudentGroup.objects.all().select_related('subject').order_by('subject__name')),
        group_id = self.request.GET.get('group_id', '')
        year = self.request.GET.get('year', '')
        month = self.request.GET.get('month', '')

        today = date.today()
        context['years'] = list(range(2024, today.year + 11))

        if month.isdigit() and year.isdigit():
            context['days'] = list(range(1, calendar.monthrange(int(year), int(month))[1] + 1))
        else:
            context['days'] = []

        if group_id.isdigit() and month.isdigit() and year.isdigit():
            context['students'] = list(CustomUser.objects.filter(student_group_id=group_id
                                                                 ).prefetch_related('student_attendance'
                                                                                    ).order_by('first_name'
                                                                                               ).values('id',
                                                                                                        'first_name',
                                                                                                        'last_name'))

            attendances = list(Attendance.objects.filter(student__student_group_id=group_id,
                                                         date__year=year,
                                                         date__month=month).values())

            for student in context['students']:
                student['attendances'] = []
                for day in context['days']:
                    for attendance in attendances:
                        if attendance['date'].day == day and attendance['student_id'] == student['id']:
                            obj = {'come': attendance['come'], 'reason': attendance['reason']}
                            break
                    else:
                        obj = {'come': '', 'reason': '', 'day': day}
                    student['attendances'].append(obj)
        else:
            context['students'] = []

        return context

    def post(self, request, *args, **kwargs):
        group_id = request.GET.get('group_id', '')
        year = request.GET.get('year', '')
        month = request.GET.get('month', '')
        day = request.POST.get('day', '')
        student_id = request.POST.get('student_id', '')
        come = request.POST.get('come', '')
        reason = request.POST.get('reason', '')
        print(request.POST)
        if not (
                group_id.isdigit() or year.isdigit() or month.isdigit() or day.isdigit() or student_id.isdigit() or come != ''):
            return redirect('attendances:student_attendance')

        if come == 'True':
            reason = ''

        form = AttendanceCreateForm(
            {'student': student_id, 'date': f'{year}-{month}-{day}', 'come': come, 'reason': reason, })

        if form.is_valid():
            form.save()

        else:
            messages.error(request, form.errors)

        return redirect(request.META['HTTP_REFERER'])