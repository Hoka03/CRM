from django import forms

from apps.users.models import CustomUser
from .models import StudentGroup
from apps.subjects.models import Subject
from apps.general.enums.weeks import WeekDay


class AddGroupForm(forms.ModelForm):
    teacher = forms.ModelChoiceField(queryset=CustomUser.objects.filter(role=CustomUser.RoleChoices.TEACHER.value),
                                     label="Teacher Name* ", widget=forms.Select(attrs={'class': 'form-control'}))
    subject = forms.ModelChoiceField(queryset=Subject.objects.all(), label="subject* ",
                                     widget=forms.Select(attrs={'class': 'select2'}))
    start_time = forms.TimeField(widget=forms.TextInput(attrs={'class': 'form-control', 'place_holder': 'HH:MM'})
                                 , label="Start Time")
    end_time = forms.TimeField(widget=forms.TextInput(attrs={'class': 'form-control', 'place_holder': 'HH:MM'}),
                               label="End Time")
    week_day = forms.MultipleChoiceField(choices=WeekDay.choices, widget=forms.CheckboxSelectMultiple,
                                         label="Week Days *")

    class Meta:
        model = StudentGroup
        fields = '__all__'