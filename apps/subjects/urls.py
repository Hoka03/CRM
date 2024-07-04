from django.urls import path

from apps.subjects.views import subjects, books


urlpatterns = [
    path('subject/', subjects.SubjectListView.as_view(), name='subject_page'),
    path('subject-delete/<int:pk>/', subjects.SubjectDeleteView.as_view(), name='subject_delete'),
    path('subject-edit/<int:pk>/', subjects.SubjectEditView.as_view(), name='subject_edit'),
    path('all-book/', books.BookListView.as_view(), name='all_book_page'),
    path('add-book/', books.AddBookTemplateView.as_view(), name='add_book_page'),
]