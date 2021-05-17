import sqlite3
from django.conf import settings
from django import forms
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate as djangoAuthenticate
from ConnectDB import c

debug = getattr(settings,'DEBUG',False)
def login(request):
   if debug:
      print("login")      
      print(request.POST)
   if 'username' not in request.POST or 'password' not in request.POST:
      error = "Entrez le nom d'utilisateur et le mot de passe"
      return render(request,'login.html',{'error': error})
   username = request.POST['username']
   password = request.POST['password']
   if debug:
      print("username " + username)
      print("password " + password)
   user = djangoAuthenticate(username=username,password=password)
   if user is not None:
      if debug:
         print(request.session)
         request.session['logged_user'] = username
      return render(request,'menu.html')
   else:
      error = "Nom d'utilisateur ou mot de passe incorrects"
      return render(request,'login.html',{'error': error})

def option1(request):
   print("option1")
   return render(request,'option1.html',{'param':c})

def option2(request):
   print("option2")
   return render(request,'option2.html')

def logout(request):
   print("logout")
   del request.session['logged_user']
   request.session.modified = True
   return redirect('login')
   