import calendar
from datetime import date

from django.views.generic import TemplateView
from .models import Attendance
from apps.groups.models import StudentGroup
from apps.users.models import CustomUser


class AttendanceListView(TemplateView):
    template_name = 'students/student-attendence.html'
    extra_context = {
        'groups': StudentGroup.objects.order_by('subject__name'),
    }

    def get_context_data(self, *args, **kwargs):
        group_id = str(self.request.GET.get('group_id'))
        month = str(self.request.GET.get('month'))
        year = str(self.request.GET.get('year'))

        context = super().get_context_data(*args, **kwargs)
        today = date.today()
        context['years'] = list(range(2024, today.year + 11))

        if month.isdigit() and year.isdigit():
            context['days'] = list(range(1, calendar.monthrange(int(year), int(month))[1] + 1))
        else:
            context['days'] = []

        if group_id.isdigit():
            context['students'] = list(CustomUser.objects.filter(student_group_id=group_id
                                                                 ).prefetch_related('attendance_set'
                                                                                    ).order_by('first_name'
                                                                                               ).values('id',
                                                                                                        'first_name',
                                                                                                        'last_name'))
            attendances = list(Attendance.objects.filter(student__student_group_id=group_id,
                                                         attendance_date__month=month,
                                                         attendance_date__year=year).values())

            for student in context['students']:
                student['attendances'] = []
                for day in context['days']:
                    for attendance in attendances:
                        if attendance['attendance_date'].day == day and attendance['student_id'] == student['id']:
                            obj = {
                                'come': attendance.get('status') == Attendance.StatusChoice.COME.value,
                                'did_not_come': attendance.get('status') == Attendance.StatusChoice.DID_NOT_COME.value,
                                'reason': attendance.get('reason', '')
                            }
                            break
                    else:
                        obj = {
                            'come': False,
                            'did_not_come': True,
                            'reason': '',
                        }
                    student['attendances'].append(obj)

        else:
            context['students'] = []

        return context

    # def get_queryset(self):
    #     group_id = self.request.GET.get('group_id')
    #     month = self.request.GET.get('month')
    #     year = self.request.GET.get('year')
    #
    #     if group_id and month and year and group_id.isdigit() and month.isdigit() and year.isdigit():
    #         queryset = Attendance.objects.filter(student__student_group_id=group_id,
    #                                              attendance_date__month=month,
    #                                              attendance_date__year=year).order_by('attendance_date__day')
    #     else:
    #         queryset = Attendance.objects.none()
    #     return queryset
