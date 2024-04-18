from django.shortcuts import HttpResponse

def homePage(request):
    return HttpResponse("Welcome to our website")