from django.shortcuts import render

from django.http import HttpResponse

# define uma view baseada em função
def index(request):
    # return HttpResponse('olá django - index')
    # return render(request, 'index.html')
    return render(request, 'index.html', {'titulo': 'últimas enquetes'})

# define outra view baseada em função
def ola(request):
    return HttpResponse('olá django')