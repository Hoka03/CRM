from django import forms

from django_ckeditor_5.widgets import CKEditor5Widget
from .models import Lesson


class LessonForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["text"].required = False

    class Meta:
        model = Lesson
        fields = ("content",)
        widgets = {
            "text": CKEditor5Widget(
                attrs={"class": "django_ckeditor_5"}, config_name="lesson"
            )
        }

