from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email=models.CharField(max_length=45)
    password=models.CharField(max_length=255)

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc=models.TextField(default='')
    uploaded_by=models.ForeignKey(User,related_name='uploaded_book',on_delete=models.CASCADE)
    users_liked_book=models.ManyToManyField(User,related_name='fav_books')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


