
from django.urls import path

from . import views

urlpatterns = [
    path('', views.books_home, name='book-home'),
    path('detail/<int:book_id>/', views.book_detail, name='book-detail'),
    path('edit/<int:book_id>/', views.book_edit, name='book-edit'),
    path('update/<int:book_id>/', views.book_update, name='book-update'),
    path('delete/<int:book_id>/', views.book_delete, name='book-delete'),
    path('add/', views.book_add, name='add-book'),
    path('insert/', views.book_insert, name='insert-book'),
]