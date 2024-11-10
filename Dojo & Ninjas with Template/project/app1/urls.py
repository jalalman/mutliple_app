from django.urls import path
from . import views


urlpatterns =[
    path('',views.index),
    path('addDojo',views.addDojo),
    path('addNinja',views.addNinja),
    path('delete/<int:id>',views.delete,name='delete'),
    path('deleten/<int:id>',views.deleten,name='deleten')
]