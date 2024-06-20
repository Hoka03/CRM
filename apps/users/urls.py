from django.urls import path
from apps.users import views

from .views import AdminDashboardTemplateView


urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('account-page/', views.AccountTemplateView.as_view(), name='account_page'),

    # Parents View
    path('parent-page/', views.ParentTemplateView.as_view(), name='parent_page'),
    path('parent-detail-page/<int:pk>/', views.ParentDetailTemplateView.as_view(), name='parent_detail_page'),
    path('add-parent-page/', views.ParentRegisterView.as_view(), name='add_parent_page'),

    # Teachers View
    path('teacher-page/', views.TeacherTemplateView.as_view(), name='teacher_page'),
    path('teacher-detail-page/<int:pk>/', views.TeacherDetailView.as_view(), name='teacher_detail_page'),
    path('add-teacher-page/', views.TeacherRegisterView.as_view(), name='add_teacher_page'),
    path('teacher-payment-page/', views.TeacherPaymentTemplateView.as_view(), name='teacher_payment_page'),

    # Students View
    path('student-page/', views.StudentTemplateView.as_view(), name='student_page'),
    path('student-detail-page/<int:pk>/', views.StudentDetailView.as_view(), name='student_detail_page'),
    path('add-student-page/', views.StudentRegisterView.as_view(), name='add_student_page'),
    path('student-promotion-page/', views.StudentPromotionTemplateView.as_view(), name='student_promotion_page'),

    # Dashboards
    path('', AdminDashboardTemplateView.as_view(), name='home'),
    path('student-dashboard-page/', views.StudentDashboardTemplateView.as_view(), name='student_dashboard_page'),
    path('parent-dashboard-page/', views.ParentDashboardTemplateView.as_view(), name='parent_dashboard_page'),
    path('teacher-dashboard-page/', views.TeacherDashboardTemplateView.as_view(), name='teacher_dashboard_page'),

    # Delete Users
    path('delete-student/<int:pk>/', views.StudentDeleteView.as_view(), name='student_delete'),
    path('delete-teacher/<int:pk>/', views.TeacherDeleteView.as_view(), name='teacher_delete'),
    path('delete-parent/<int:pk>/', views.ParentDeleteView.as_view(), name='parent_delete'),

    # Edit Users
    path('edit-student<int:pk>/', views.StudentEditView.as_view(), name='student_edit'),
    path('edit-teacher<int:pk>/', views.TeacherEditView.as_view(), name='teacher_edit'),
    path('edit-parent<int:pk>/', views.ParentEditView.as_view(), name='parent_edit'),
]