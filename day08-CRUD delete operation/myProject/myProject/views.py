from django.shortcuts import redirect, render
from myApp.models import StudentModel


def studentPage(request):
    student=StudentModel.objects.all()
    studentDict={
        'student':student
    }
    return render(request, 'studentPage.html', studentDict)

def addStudent(request):
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
    student=StudentModel.objects.get(id=myid)
    student.delete()
    return redirect('studentPage')