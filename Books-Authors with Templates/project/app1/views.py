from django.shortcuts import render ,redirect
from . import models
# Create your views here.

def index(request):
    context={
        'books':models.get_all_books()
    }

    return render(request,'index.html',context)


def authors(request):
    context={
        'authors':models.get_all_authors,
        
    }

    return render(request,'authors.html',context)


def authorsview(request,id):
    context={
        'authors':models.get_author_by_id(id),
        'books':models.get_all_books(),
    }

    return render(request,'authorsv.html',context)


def addbook(request):

    models.add_new_book(request.POST)

    return redirect ('/')



def bookpage(request,id):
    context={
        'book':models.get_book_by_id(id),
        'authors':models.get_all_authors()
    }
    return render(request,'books.html',context)


def addauthor(request):
    models.add_new_author(request.POST)

    return redirect('/authors')


def addBookAuthor(request):
    models.add_book_to_author(request.POST)
    id = request.POST['author_id']
    return redirect("/authordesc/"+id)


def addAuthorBook(request):
    models.add_author_to_Book(request.POST)
    id =request.POST['book_id']
    return redirect('/bookdesc/'+id)