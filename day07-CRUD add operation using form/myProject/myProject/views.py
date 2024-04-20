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