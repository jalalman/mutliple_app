from django.urls import path
from . import views


urlpatterns=[
    path('',views.usersindex),
    path('register',views.register),
    path('login',views.login),
    path('users/new',views.news),
    path('users',views.display)
]