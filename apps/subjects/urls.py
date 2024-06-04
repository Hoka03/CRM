from django.urls import path

from .views import home, SubjectListView, DetailView

urlpatterns = [
    # path('', home, name='home'),
    path('', SubjectListView.as_view(), name='home'),
    path('<int:pk>/', DetailView.as_view(), name='subject_detail'),
]