from django.shortcuts import render,redirect

def teacherdashboard(request):
    return render(request,'teacher/teacherdashboard.html')

def teacherlist(request):
    return render(request,'teacher/teacherlist.html')

def teacheradd(request):
    return render(request,'teacher/teacheradd.html')

def teacherdetails(request):
    return render(request,'teacher/teacherdetails.html')

def teacheredit(request):
    return render(request,'teacher/teacheredit.html')

def teacherdelete(request):
    return redirect('teacherlist')