from django.shortcuts import render

import requests
from django.shortcuts import redirect
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django import forms
import json
import hashlib


# Create your views here.


url = "https://simsvendapi-production.up.railway.app/"

class EditForm(forms.Form):    
    id = forms.CharField(label = "id", required=True)
    elo = forms.CharField(label = "Elo",required=False)
    points = forms.CharField(label = "Points",required=False)

class TourForm(forms.Form):
    name = forms.CharField(label = "Navn",required=True)
    how_many = forms.IntegerField(label = "How_many",required=True)
    place_id = forms.IntegerField(label = "Place_ID",required=True)
    gender = forms.CharField(label = "Køn",required=True)
    PricePool = forms.IntegerField(label = "PricePool",required=True)
    Dec = forms.CharField(label="Description", required=True)
    


    
   






def index(request):
    

    if request.session.get('role') == 2:      

 
        return render(request, "web_admin/index.html",{          
        
    })
    
    else:
  
        return HttpResponseRedirect(reverse("login")) 



def users(request):

    if request.session.get('role') == 2:     

        return render(request, "web_admin/users.html",{

            "form" : EditForm

        })
    else:
  
        return HttpResponseRedirect(reverse("login")) 


def matches(request):

    if request.session.get('role') == 2:     

        return render(request, "web_admin/matches.html")


    else:
  
        return HttpResponseRedirect(reverse("login")) 
        



def tournements(request):

    if request.session.get('role') == 2:     

        return render(request, "web_admin/tournements.html", {


            "form" : TourForm,

        })


    else:
  
        return HttpResponseRedirect(reverse("login")) 

def login(request):


    if request.method == "POST":
        # Attempt to sign user in


        email = request.POST["email_test"]
        password = request.POST["password"]   
        

        myobj = {'email': "t.kronborg6@gmail.com", "password" : "Test"}
        x = requests.post(url + "user/login", json = myobj)   
        json_response = x.json()

       
        role = json_response[0]["RoleID"]
        
        session = requests.session()    
        request.session['role'] = role        
        



        return HttpResponseRedirect(reverse("index"))    


        

    else:

        return render(request, "web_admin/login.html")

def logout(request):


    request.session['role'] = ""
   

    return HttpResponseRedirect(reverse("login"))  