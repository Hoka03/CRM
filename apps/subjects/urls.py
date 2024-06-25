from django.urls import path

from .views import SubjectListView, BookListView, AddBookTemplateView


urlpatterns = [
    path('subject/', SubjectListView.as_view(), name='subject_page'),
    path('all-book/', BookListView.as_view(), name='all_book_page'),
    path('add-book/', AddBookTemplateView.as_view(), name='add_book_page'),
]