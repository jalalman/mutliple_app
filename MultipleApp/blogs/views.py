from django.shortcuts import render , HttpResponse ,redirect

# Create your views here.
def index(request):


    return HttpResponse('placeholder to display a list of all blogs')

def new(request):

    return HttpResponse('placeholder to display a new form to create a new blog')


def create(request):

    return redirect('/blogs')

def edit(request,number):

    return HttpResponse(f"placeholder to edit blog {number}")

def delete(request,number):

    return redirect('/blogs')