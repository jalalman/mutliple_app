from django.urls import path
from . import views

urlpatterns=[
    path('',views.index),
    path('shows',views.shows ,name='show'),
    path('addAnewpage',views.addAnewpage,name='addAnewpage'),
    path('createshow',views.createshow,name='createshow'),
    path('shows/<int:id>',views.displayShow,name='displayShow'),
    path('shows/<int:id>/edit',views.render_editshow,name='render_editshow'),
    path('confirmedit',views.confirmedit,name='confirmedit'),
    path('deleteshow/<int:id>',views.deleteshow,name='deleteshow')

]