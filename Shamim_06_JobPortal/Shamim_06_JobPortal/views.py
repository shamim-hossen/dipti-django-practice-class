from django.shortcuts import redirect, render



def signup(request):

    return render(request, 'signup.html')

def signin(request):

    return render(request, 'signin.html')