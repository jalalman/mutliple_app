from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=255)
    desc=models.TextField(default="")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Author(models.Model):
    first_name=models.CharField(max_length=45)
    last_name=models.CharField(max_length=45)
    notes=models.TextField(default="")
    books=models.ManyToManyField(Book,related_name='authors')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


def add_new_book(data):
    Book.objects.create(title=data['title'],desc=data['desc'])


def get_all_books():

    return Book.objects.all()

def get_book_by_id(id):

    return Book.objects.get(id=id)


def add_new_author(data):

    Author.objects.create(first_name=data['fname'],last_name=data['lname'],notes=data['note'])

def get_all_authors():

    return Author.objects.all()

def get_author_by_id(id):
    
    return Author.objects.get(id=id)

def get_book_by_id(id):

    return Book.objects.get(id=id)

def add_book_to_author(data):

    this_book=Book.objects.get(id=int(data['book_id']))
    this_author=Author.objects.get(id=int(data['author_id']))
    this_book.authors.add(this_author)


def add_author_to_Book(data):
    this_book=Book.objects.get(id=int(data['book_id']))
    print(this_book)
    this_author=Author.objects.get(id=int(data['author_id']))
    print(this_author)
    this_author.books.add(this_book)
