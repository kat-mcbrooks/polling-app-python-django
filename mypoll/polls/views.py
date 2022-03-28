from django.shortcuts import render

from .models import Question, Choice

# get questions and display them
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]  # 5 questions, descending order by date
    # in order to pass in the questions to the template, we use a dictionary. Common convention is to call this variable context
    context = {"latest_question_list: latest_question_list"}
    return render(request, "polls/index.html", context)
