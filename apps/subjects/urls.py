from django.urls import path

from .views import SubjectListView, SubjectFormView

urlpatterns = [
    # path('', SubjectListView.as_view(), name='home'),
    path('', SubjectFormView.as_view(), name='home'),
    path('success/', SubjectListView.as_view(template_name='subject_success.html'), name='subject_success')
]
