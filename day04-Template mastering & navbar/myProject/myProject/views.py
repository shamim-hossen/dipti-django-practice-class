from django.shortcuts import render

def studentPage(request):
    return render(request, 'studentPage.html')

def home(request):
    return render(request, 'home.html')

def news(request):
    return render(request, 'news.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')