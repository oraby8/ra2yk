from django.shortcuts import render
from .forms import QuestionForm
from django.core.paginator import Paginator
from django.shortcuts import redirect

from .models import Question


def index(request):
    context ={}
  
    # create object of form
    form = QuestionForm(request.POST or None, request.FILES or None)

      
    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        D=form.save()
        id_=D.id
        return redirect(f'/questions/{id_}/')
    result = Question.objects.filter(public=True)
  
    context['form']= form
    context['result']=result
    return render(request, "index.html", context)

def questions(request,pk):
    context ={}
    result=Question.objects.filter(id=pk).first()
    context['result']=result
    return render(request, "question.html", context)

def answer(request,pk):

    context ={}
    result=Question.objects.filter(id=pk).first()
    context['result']=result
    return render(request, "answer.html", context)


def templates(request):
    context ={}
    result=Question.objects.filter(public=True)
    context['result']=result
    return render(request, "temp.html", context)
