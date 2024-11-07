from django.shortcuts import render ,HttpResponse ,redirect

# Create your views here.


def usersindex(request):
    return HttpResponse('users')



def register(request):

    return HttpResponse('placeholder for users to create a new user record')

def login(request):

    return HttpResponse("placeholder for users to log in")

def news(request):

    return redirect('users/register')

def display(request):

    return HttpResponse("placeholder to display all the list of users later.")