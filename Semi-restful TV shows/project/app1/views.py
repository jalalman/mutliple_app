from django.shortcuts import render ,redirect
from . import models

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
    models.updateShow(request.POST)

    return redirect(f"shows/{int(request.POST['show_id'])}")


def deleteshow(request,id):
    id =int(id)
    models.deleteShow(id)

    return redirect('/')
