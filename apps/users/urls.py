from django.urls import path

from .views import UserLoginView, UserLogoutView, StudentDetailView


urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('student-detail/', StudentDetailView.as_view(), name='student_detail'),
]