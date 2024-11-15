from django.urls import path

from . import views


urlpatterns=[

    path('',views.home,name='home'),
    path('regAcc',views.regAcc,name='regAcc'),
    path('confirmlogin',views.confirmlogin,name='confirmlogin'),
    path('success',views.suclogin,name='suclogin'),
    path('logout',views.logout,name='logout')

]