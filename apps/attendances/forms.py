from django.forms import ModelForm
from apps.attendances.models import Attendance


class AttendanceCreateForm(ModelForm):
    class Meta:
        model = Attendance
        fields = '__all__'
