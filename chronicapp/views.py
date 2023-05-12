from django.shortcuts import render

# Create your views here.

#from django.http import HttpResponse
#def home(request):
    #return HttpResponse('<h1>SANITAS HOME</h1>')


def Home(request):
    return render(request,'chronicapp/home.html')

def About(request):
    return render(request,'chronicapp/about.html')

def Solutions(request):
    return render(request,'chronicapp/solutions.html')

def Products(request):
    return render(request,'chronicapp/products.html')

def Groups(request):
    return render(request,'chronicapp/groups.html')

def Reminders(request):
    return render(request,'chronicapp/reminders.html')

def Login(request):
    return render(request,'chronicapp/login.html')


def Register(request):
    return render(request,'chronicapp/register.html')








