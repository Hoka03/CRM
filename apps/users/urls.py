from django.urls import path

from .views import (UserLoginView, UserLogoutView, AccountTemplateView, ParentTemplateView, ParentDetailTemplateView,
                    AddParentTemplateView, TeacherTemplateView, TeacherDetailView, AddTeacherTemplateView,
                    TeacherPaymentTemplateView, StudentTemplateView, StudentRegisterView,
                    StudentPromotionTemplateView, StudentDashboardTemplateView, ParentDashboardTemplateView,
                    TeacherDashboardTemplateView, AdminDashboardTemplateView)


urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('account-page/', AccountTemplateView.as_view(), name='account_page'),
    #For Parents
    path('parent-page/', ParentTemplateView.as_view(), name='parent_page'),
    path('parent-detail-page/', ParentDetailTemplateView.as_view(), name='parent_detail_page'),
    path('add-parent-page/', AddParentTemplateView.as_view(), name='add_parent_page'),
    #For Teachers
    path('teacher-page/', TeacherTemplateView.as_view(), name='teacher_page'),
    path('teacher-detail-page/', TeacherDetailView.as_view(), name='teacher_detail_page'),
    path('add-teacher-page/', AddTeacherTemplateView.as_view(), name='add_teacher_page'),
    path('teacher-payment-page/', TeacherPaymentTemplateView.as_view(), name='teacher_payment_page'),
    #For Students
    path('student-page/', StudentTemplateView.as_view(), name='student_page'),
    path('add-student-page/', StudentRegisterView.as_view(), name='add_student_page'),
    path('student-promotion-page/', StudentPromotionTemplateView.as_view(), name='student_promotion_page'),
    #Dashboards
    path('', AdminDashboardTemplateView.as_view(), name='admin_dashboard_page'),
    path('student-dashboard-page/', StudentDashboardTemplateView.as_view(), name='student_dashboard_page'),
    path('parent-dashboard-page/', ParentDashboardTemplateView.as_view(), name='parent_dashboard_page'),
    path('teacher-dashboard-page/', TeacherDashboardTemplateView.as_view(), name='teacher_dashboard_page'),
]