from django.urls import path

from . import views

urlpatterns = [
    path("", views.transaction_list_view, name="transaction_list"),
    path("issue/", views.issue_book_view, name="issue_book"),
    path("<int:pk>/return/", views.return_book_view, name="return_book"),
]
