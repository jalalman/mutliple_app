from django.shortcuts import render ,redirect
from . import models
from django.contrib import messages
from .models import Show
# Create your views here.
def index(request):

    return redirect('/shows')

def shows(request):
    context={
        "shows":models.get_all_shows()
    }

    return render(request,'shows.html',context)

def addAnewpage(request):

    return render(request,'addnewShow.html')


def createshow(request):
    if request.method=="POST":
        errors=Show.objects.basic_validator(request.POST)
        if len(errors)>0:
            for key,value in errors.items():
                messages.error(request,value)
            return redirect('/addAnewpage')


        user=models.create_show(request.POST)
        return redirect(f'shows/{user.id}')

def displayShow(request,id):
    context={
        "show":models.get_show(id)
    }
    return render(request,'viewshow.html',context)


def render_editshow(request,id):
    id= int(id)
    context={
        "show":models.get_show(id)
    }
    return render(request,'editshow.html',context)

def confirmedit(request):
    if request.method=="POST":
        errors=Show.objects.basic_validator(request.POST)
        if len(errors)>0:
            for key,value in errors.items():
                messages.error(request,value)
            return redirect(f'shows/{int(request.POST['show_id'])}/edit')

    models.updateShow(request.POST)

    return redirect(f"shows/{int(request.POST['show_id'])}")


def deleteshow(request,id):
    id =int(id)
    models.deleteShow(id)

    return redirect('/')
