from django.urls import path

from . import views


urlpatterns=[
    path('',views.index),
    path('addbook',views.addbook),
    path ('authors',views.authors),
    path('addauthor',views.addauthor),
    path('authordesc/<int:id>',views.authorsview,name='authordesc'),
    
    path('bookdesc/<int:id>',views.bookpage,name='bookdesc'),
    path('add_book_author',views.addBookAuthor),
    path('add_auth_book',views.addAuthorBook)
]