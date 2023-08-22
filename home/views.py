from django.shortcuts import render
from django.http import HttpResponse
from  . forms import loginform,signupform,memberform
from . models import Books

# Create your views here.
def index(request):
    return render(request,'index.html')
def login(request):
    form=loginform()
    dict_form={
        "form": form
    }
    return render(request,'login.html',dict_form)
def signup(request):
    form=signupform()
    dict_form1={
        
        "form":form
    }
    return render(request,'signup.html',dict_form1)
def books(request):
    form=memberform()
    dict_bok={
        'books':Books.objects.all()
    }
    return render(request,'books.html',dict_bok)
def members(request):
    if request.method=="POST":
        form= memberform(request.POST)
        if form.is_valid():
            form.save()
        
    form=memberform()
    dict_form2={
        
        "form":form
    }
    return render(request,'members.html',dict_form2)