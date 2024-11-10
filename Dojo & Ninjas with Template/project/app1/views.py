from django.shortcuts import render ,HttpResponse,redirect
from . import models
from .models import Dojo, Ninja
# Create your views here.


def index(request):
    context={
        'dojos':models.getAllDojo(),
    }
    return render(request,'index.html',context)


def addDojo(request):
    models.create_Dojo(request.POST)


    return redirect ('/')


def addNinja(request):
    models.create_ninja(request.POST)

    return redirect('/')

def delete(request,id):
    models.deleteDojo(id)

    return redirect('/')

def deleten(request,id):
    models.deleteNinja(id)

    return redirect('/')