from django.db.models.query_utils import Q
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Choice, Question
from django.template import loader
from django.urls import reverse
# Create your views here.


from django.http import HttpResponse

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    print(type(latest_question_list),"Type of queryset")
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context,request))


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question':question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request,'polls/results.html',{'question':question})

    
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        abc = Choice.objects.filter(question__pub_date="2021-03-23")
        print(abc)
    except (KeyError, Choice.DoesNotExist):

        return render(request,'polls/detail.html',{
            'question':question,
            'error_message':"You didn't select a choice. ",
        })
 
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))