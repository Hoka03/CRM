from django import forms

from .models import ExamResult


class ExamResultForm(forms.ModelForm):
    class Meta:
        model = ExamResult
        fields = ['exam', 'grade_point', 'percent', 'comment']