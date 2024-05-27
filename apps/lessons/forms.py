from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from apps.lessons.models import Lesson


class LessonForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget(config_name='design'))

    class Meta:
        model = Lesson
        fields = 'content'