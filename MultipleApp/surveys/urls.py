from django.urls import path
from . import views

urlpatterns=[
    path('',views.surveysindex),
    path('new',views.surveysnew)
]