from django.urls import path
from .views import (
    AuthorListView, AuthorCreateView, AuthorUpdateView, AuthorDeleteView,
    BookListView, BookCreateView, BookUpdateView, BookDeleteView,
    BorrowRecordListView, BorrowRecordCreateView, BorrowRecordUpdateView, BorrowRecordDeleteView,
    export_authors_excel, export_books_excel, export_borrowrecords_excel, library_dashboard
)

urlpatterns = [
    # Home page URL
    path('', library_dashboard, name='library-dashboard'),
    
    # Author URLs
    path('authors/', AuthorListView.as_view(), name='author-list'),
    path('authors/add/', AuthorCreateView.as_view(), name='add-author'),
    path('authors/edit/<int:pk>/', AuthorUpdateView.as_view(), name='edit-author'),
    path('authors/delete/<int:pk>/', AuthorDeleteView.as_view(), name='delete-author'),

    # Book URLs
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/add/', BookCreateView.as_view(), name='add-book'),
    path('books/edit/<int:pk>/', BookUpdateView.as_view(), name='edit-book'),
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='delete-book'),

    # BorrowRecord URLs
    path('borrows/', BorrowRecordListView.as_view(), name='borrow-list'),
    path('borrows/add/', BorrowRecordCreateView.as_view(), name='add-borrow'),
    path('borrows/edit/<int:pk>/', BorrowRecordUpdateView.as_view(), name='edit-borrow'),
    path('borrows/delete/<int:pk>/', BorrowRecordDeleteView.as_view(), name='delete-borrow'),

    # Export
    path('export-authors/', export_authors_excel, name='export-authors'),
    path('export-books/', export_books_excel, name='export-books'),
    path('export-borrows/', export_borrowrecords_excel, name='export-borrows'),
]
