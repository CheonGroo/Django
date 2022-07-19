from django.http import Http404
from django.http import HttpResponse, request
from django.shortcuts import render
from . import models


def index(req):
    latest_question_list = models.Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(req, 'polls/index.html', context)

def detail(req, question_id):
    question = models.Question.objects.filter(pk=question_id)
    if len(question) == 0:
        raise Http404("Question does not exist")
    return render(req,'polls/detail.html', {'question':question[0]})

def results(req, question_id):
    response = "You're looking at the results of question {0}. {1} {0}"
    return HttpResponse(response.format(question_id,"aaa"))

def vote(req, question_id):
    return HttpResponse(f"You're voting on question {question_id}.")