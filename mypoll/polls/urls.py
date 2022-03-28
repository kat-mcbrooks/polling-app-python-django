from django.urls import path
from . import views

app_name = "polls"  # we specify here the name of the app because we might have same-named urls within different apps
urlpatterns = [
    # route at /polls/
    path("", views.index, name="index")
]  # essentially, here we are creating a route. First arg is empty because we want the route to be polls
