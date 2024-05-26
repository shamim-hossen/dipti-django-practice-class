from django.shortcuts import render,redirect


def signinPage(request):


    return render(request,"Common/signinPage.html")


def signupPage(request):


    return render(request,"Common/signupPage.html")

