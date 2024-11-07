from django.shortcuts import render ,HttpResponse

# Create your views here.
def surveysindex(request):

    return HttpResponse('placeholder to display all the surveys created')


def surveysnew(request):

    return HttpResponse("placeholder for users to add a new survey")
