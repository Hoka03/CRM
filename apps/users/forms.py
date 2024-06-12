from django import forms

from .models import CustomUser


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()


class AddStudentForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['role', 'gender', 'first_name', 'last_name', 'date_of_birth', 'email', 'photo',
                  'student_group', 'phone_number']
