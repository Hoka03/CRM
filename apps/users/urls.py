from django.urls import path
from apps.users import views

from .views import students, parents, teachers, admins


urlpatterns = [
    path('login/', views.admins.UserLoginView.as_view(), name='login'),
    path('logout/', views.admins.UserLogoutView.as_view(), name='logout'),
    path('account-page/', views.admins.AccountTemplateView.as_view(), name='account_page'),

    # Parents View
    path('parent-page/', views.parents.ParentTemplateView.as_view(), name='parent_page'),
    path('parent-detail-page/<int:pk>/', views.parents.ParentDetailTemplateView.as_view(),
         name='parent_detail_page'),
    path('add-parent-page/', views.parents.ParentRegisterView.as_view(), name='add_parent_page'),

    # Teachers View
    path('teacher-page/', views.teachers.TeacherTemplateView.as_view(), name='teacher_page'),
    path('teacher-detail-page/<int:pk>/', views.teachers.TeacherDetailView.as_view(), name='teacher_detail_page'),
    path('add-teacher-page/', views.teachers.TeacherRegisterView.as_view(), name='add_teacher_page'),
    path('teacher-payment-page/', views.teachers.TeacherPaymentTemplateView.as_view(), name='teacher_payment_page'),

    # Students View
    path('student-page/', views.students.StudentTemplateView.as_view(), name='student_page'),
    path('student-detail-page/<int:pk>/', views.students.StudentDetailView.as_view(), name='student_detail_page'),
    path('add-student-page/', views.students.StudentRegisterView.as_view(), name='add_student_page'),
    path('student-promotion-page/', views.students.StudentPromotionTemplateView.as_view(),
         name='student_promotion_page'),

    # Dashboards
    path('', views.admins.AdminDashboardTemplateView.as_view(), name='home'),
    path('student-dashboard-page/', views.students.StudentDashboardTemplateView.as_view(),
         name='student_dashboard_page'),
    path('parent-dashboard-page/', views.parents.ParentDashboardTemplateView.as_view(),
         name='parent_dashboard_page'),
    path('teacher-dashboard-page/', views.teachers.TeacherDashboardTemplateView.as_view(),
         name='teacher_dashboard_page'),

    # Delete Users
    path('delete-student/<int:pk>/', views.students.StudentDeleteView.as_view(), name='student_delete'),
    path('delete-teacher/<int:pk>/', views.teachers.TeacherDeleteView.as_view(), name='teacher_delete'),
    path('delete-parent/<int:pk>/', views.parents.ParentDeleteView.as_view(), name='parent_delete'),

    # Edit Users
    path('edit-student<int:pk>/', views.students.StudentEditView.as_view(), name='student_edit'),
    path('edit-teacher<int:pk>/', views.teachers.TeacherEditView.as_view(), name='teacher_edit'),
    path('edit-parent<int:pk>/', views.parents.ParentEditView.as_view(), name='parent_edit'),
]