from django.shortcuts import redirect, render
from myApp.models import showModel
# Home, News, Contact, About
def homepage(request):
    student=showModel.objects.all()
    stdDict={
        'student':student,
    }
    return render(request, 'homepage.html', stdDict)

def newspage(request):
    return render(request, 'newspage.html')

def contactpage(request):
    return render(request, 'contactpage.html')

def aboutpage(request):
    return render(request, 'aboutpage.html')



