from django.http import HttpResponse
from django.shortcuts import render

def pingpong(request):
    return render(request, 'pong.html')

def index(request):
    name = request.GET.get('name')
    return render(request, 'index.html')

def recieve(request):
    print(request.POST.get('todo'))
    return HttpResponse('ok')