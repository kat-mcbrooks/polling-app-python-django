from django.urls import path
from . import views

# app_name = "pages"  # we specify here the name of the app because we might have same-named urls within different apps
urlpatterns = [
    path("", views.index, name="index"),
]
