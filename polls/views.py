from django.shortcuts import render

from django.http import HttpResponse

from polls.models import Question

# define uma view baseada em função
def index(request):
    # return HttpResponse('olá django - index')
    # return render(request, 'index.html')
    return render(request, 'index.html', {'titulo': 'Gerenciamento de fornecedores'})

# define outra view baseada em função
def ola(request):
    # return HttpResponse('olá django')
    questions = Question.objects.all()
    context = {'all_questions': questions}
    return render(request, 'polls/questions.html', context)
