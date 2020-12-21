from django.urls import path
from . import views


urlpatterns = [
    path("", views.index),
    path("profile/<str:username>", views.account_profile),
    path("profile/", views.account_profile),
    path("project/add", views.add_project),
    path("project/edit/<str:project_name>", views.edit_project),
    path("project/view/<str:project_name>", views.view_project),
]
