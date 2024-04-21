from django.shortcuts import redirect, render
from myApp.models import StudentModel
def studentPage(request):
    student=StudentModel.objects.all()
    studentDict={
        'student':student
    }
    return render(request, 'studentPage.html', studentDict)

def addStudent(request):
    # addstudent a if form er req method=='POST' 
    # html er field var nibo then studentmodel er vitor dibo
    if request.method=='POST':
        name=request.POST.get('fname')
        roll=request.POST.get('roll')
        dept=request.POST.get('dept')
        
        student=StudentModel(
            Name=name,
            Roll=roll,
            Dept=dept,
        )
        student.save()
        return redirect('studentPage')
    return render(request, 'addStudent.html')

def deleteStudent(request, myid):
    delStudent=StudentModel.objects.get(id=myid)
    delStudent.delete()
    return redirect('studentPage')

def editStudent(request, myid):
    student=StudentModel.objects.filter(id=myid)
    studentDict={
        'student':student,
    }
    return render(request, 'editStudent.html', studentDict)

def updateStudent(request):
    if request.method=='POST':
        myid=request.POST.get('myid')
        fname=request.POST.get('fname')
        roll=request.POST.get('roll')
        dept=request.POST.get('dept')

        student=StudentModel(
            id=myid,
            Name=fname,
            Roll=roll,
            Dept=dept,
        )
        student.save()
    return redirect('studentPage')

def viewStudent(request, myid):
    student=StudentModel.objects.filter(id=myid)
    studentDict={
        'student':student,
    }
    return render(request, 'viewStudent.html', studentDict)