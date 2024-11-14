from django.shortcuts import render ,redirect
from django.contrib import messages
from .models import *
from . import models
# Create your views here.
def index(request):
    context={
        "courses":models.get_all_course()
    }
    return render(request,'index.html',context)

def addcourse(request):
    if request.method=="POST":
        errors= Course.objects.basic_validator(request.POST)
        if len(errors)>0:
            for key,value in errors.items():
                messages.error(request,value)
            return redirect('/')
    models.createCourse(request.POST)
    return redirect('/')

def destorycourses(request,id):
    context={
        'course':get_course_id(id)
    }

    return render(request,'deletepage.html',context)


def confirmdelete(request,id):

    models.deleteCourse(id)

    return redirect('/')