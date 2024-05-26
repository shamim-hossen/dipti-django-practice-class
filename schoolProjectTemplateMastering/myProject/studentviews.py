from django.shortcuts import render,redirect

def studentdashboard(request):
    return render(request,'Student/studentdashboard.html')
