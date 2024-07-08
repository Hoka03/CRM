from django import forms

from apps.subjects.models import Subject, Resource


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'


class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['book_name', 'subject', 'confirmed_by', 'published_at']