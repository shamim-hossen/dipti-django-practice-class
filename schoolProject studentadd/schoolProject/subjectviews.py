from django.shortcuts import render,redirect

def subjectslist(request):
    return render(request,'subject/subjectslist.html')

def subjectsadd(request):
    return render(request,'subject/subjectsadd.html')

def subjectsedit(request):
    return render(request,'subject/subjectsedit.html')

def subjectsdelete(request):
    return redirect('subjectslist')