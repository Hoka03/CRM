from django.urls import path

from .views import SubjectTemplateView, BookTemplateView, AddBookTemplateView


urlpatterns = [
    path('subject/', SubjectTemplateView.as_view(), name='subject_page'),
    path('all-book/', BookTemplateView.as_view(), name='all_book_page'),
    path('add-book/', AddBookTemplateView.as_view(), name='add_book_page'),
]