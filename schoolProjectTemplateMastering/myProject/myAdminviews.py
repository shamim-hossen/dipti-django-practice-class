from django.shortcuts import render, redirect

def adminDashboard(request):

    return render(request,'myAdmin/admindashboard.html')

def studentlist(request):
    return render(request,'Student/studentlist.html')

def studentadd(request):
    return render(request,'Student/studentadd.html')

def studentedit(request):
    return render(request,'Student/studentedit.html')

def teacherlist(request):
    return render(request,'Teacher/teacherlist.html')

def teacheradd(request):
    return render(request,'Teacher/teacheradd.html')

def teacheredit(request):
    return render(request,'Teacher/teacheredit.html')

def departmentlist(request):
    return render(request,'Department/departmentlist.html')

def departmentadd(request):
    return render(request,'Department/departmentadd.html')

def departmentedit(request):
    return render(request,'Department/departmentedit.html')

def subjectlist(request):
    return render(request,'Subject/subjectlist.html')

def subjectadd(request):
    return render(request,'Subject/subjectadd.html')

def subjectedit(request):
    return render(request,'Subject/subjectedit.html')