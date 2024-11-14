from django.shortcuts import render

from django.http import HttpResponse

from polls.models import Question

from django.contrib.auth.decorators import login_required

from django.contrib import messages

# define uma view baseada em função
def index(request):
    # return HttpResponse('olá django - index')
    # return render(request, 'index.html')
    aviso = 'Aviso: essa página não exige login'
    messages.warning(request, aviso)
    return render(request, 'index.html', {'titulo': 'Gerenciamento de fornecedores'})

# define outra view baseada em função
# usando o decorator de login:
@login_required
def ola(request):
    # return HttpResponse('olá django')
    questions = Question.objects.all()
    context = {'all_questions': questions}
    aviso = 'Aviso: essa página não exige login'
    messages.warning(request, aviso)
    return render(request, 'polls/questions.html', context)
