from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404

from .models import Question, Choice

# get questions and display them
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]  # 5 questions, descending order by date
    # in order to pass in the questions to the template, we use a dictionary. Common convention is to call this variable context
    context = {"latest_question_list": latest_question_list}
    # the render function returns an HttpResponse object of the given template(2nd arg) rendered with the given context(3rd arg)
    return render(request, "polls/index.html", context)


# get and show specific question and choices:
def detail(request, question_id):
    try:
        question = Question.objects.get(
            pk=question_id
        )  # this question_id will come from the url. Get the Q from the sqlite db
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/results.html", {"question": question})


# Get specific question and show results:
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})
