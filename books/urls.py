from django.urls import path

from . import views

urlpatterns = [
    path("", views.book_list_view, name="book_list"),
    path("new/", views.book_create_view, name="book_create"),
    path("<int:pk>/edit/", views.book_update_view, name="book_edit"),
    path("<int:pk>/delete/", views.book_delete_view, name="book_delete"),
]
