from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('addcourse',views.addcourse,name='addcourse'),
    path('courses/destroy/<int:id>',views.destorycourses,name='destorycourses'),
    path('courses/confirmdelete/<int:id>',views.confirmdelete,name='confirmdelete')
]
