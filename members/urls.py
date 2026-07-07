from django.urls import path

from . import views

urlpatterns = [
    path("", views.member_list_view, name="member_list"),
    path("new/", views.member_create_view, name="member_create"),
    path("<int:pk>/edit/", views.member_update_view, name="member_edit"),
    path("<int:pk>/delete/", views.member_delete_view, name="member_delete"),
]
