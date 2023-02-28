from django.shortcuts import render

# Create your views here.



def index(request):

    return render(request, "web_admin/index.html",{           
        
    })


def users(request):

    return render(request, "web_admin/users.html")


def matches(request):

    return render(request, "web_admin/matches.html")



def login(request):

    return render(request, "web_admin/login.html")


