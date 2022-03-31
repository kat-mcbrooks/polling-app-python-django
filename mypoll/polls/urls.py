from django.urls import path
from . import views

app_name = "polls"  # we specify here the name of the app because we might have same-named urls within different apps
urlpatterns = [
    # route at /polls/
    path("", views.index, name="index"),
    # e.g. /polls/5
    path("<int:question_id>/", views.detail, name="detail"),
    # use angle brackets to 'capture' this part of the url and sends it as a keyword arg to the relevant function in views.py
    # # e.g. /polls/5/results
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
