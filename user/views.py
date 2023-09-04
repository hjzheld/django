from django.http import HttpResponse
from django.shortcuts import redirect, render
from user.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

# Create your views here.
def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        User.objects.create_user(username=username, password=password)
        return redirect("/todo/")
    elif request.method == "GET":
        return render(request, "user/signup.html")
      
      
        
def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect("/todo/")
        else:
            return HttpResponse("Invaild auth", status=401)
    elif request.method == "GET":
        return render(request, "user/login.html")
    else:
        return HttpResponse("Invaild auth", status=401)


def logout(request):
    if request.method == "POST":
        auth_logout(request)
        return redirect("/todo/")
    else:
        return HttpResponse("Invaild auth method", status=405)   
