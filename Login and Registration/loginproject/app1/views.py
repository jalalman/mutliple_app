from django.shortcuts import render ,HttpResponse ,redirect
from django.contrib import messages
import bcrypt
from .models import User
from . import models
# Create your views here.
def home(request):


    return render(request,'loginandreg.html')


def regAcc(request):
    if request.method=="POST":
        errors=User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key,value in errors.items():
                messages.error(request,value)

            return redirect('/')

        else:
            models.addUser(request.POST)
            return redirect('/')

def confirmlogin(request):
    if request.method=="POST":
        email=User.objects.filter(email=request.POST['email']).first()

        if email:
            if bcrypt.checkpw(request.POST['password'].encode(),email.password.encode()):
                request.session['fname']=email.first_name

                return redirect('/success')

    return redirect('/')


def suclogin(request):

    return render(request,'success.html')

def logout(request):
    request.session.flush()
    return redirect('/')