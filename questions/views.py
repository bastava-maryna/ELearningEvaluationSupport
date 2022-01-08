from django.http import HttpResponse
from django.shortcuts import render
from questions.models import Answer
import json


# Create your views here.
def say_hello(request):
    results = Answer.objects.select_related('question').filter(question__test_id=request.GET['test_id'])
    questions = {}
    for result in results:
        if result.question.question_id in questions.keys():
            questions[result.question.question_id]['answer'].append(result.answer_text)

        else:
            questions[result.question.question_id] = {'text' : result.question.question_text, 'type' : result.question.question_type.question_type, 'answer' : [result.answer_text]}

    return HttpResponse(json.dumps(questions, indent=4))