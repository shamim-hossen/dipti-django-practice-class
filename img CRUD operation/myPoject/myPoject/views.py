from django.shortcuts import redirect, render
from myApp.models import StudentModel

def student(request):
    student=StudentModel.objects.all()
    contex={
        'student':student,
    }
    return render(request, 'student.html',contex)

def addstudent(request):
    if request.method=='POST':
        img=request.FILES.get('img')
        firstname=request.POST.get('firstname')
        roll=request.POST.get('roll')
        dept=request.POST.get('dept')
        city=request.POST.get('city')

        student=StudentModel(
            ProfilePic=img,
            Name=firstname,
            Roll=roll,
            Department=dept,
            City=city,
        )
        student.save()
        return redirect('student')
    return render(request, 'addstudent.html')

def delstudent(request,myid):
    student=StudentModel.objects.get(id=myid)
    student.delete()
    return redirect('student')

def editstudent(request, myid):
    student=StudentModel.objects.filter(id=myid)
    contex={
        'student':student,
    }
    return render(request, 'editstudent.html',contex)

def updatestudent(request):
    if request.method=='POST':
        myid=request.POST.get('myid')
        img=request.FILES.get('img')
        firstname=request.POST.get('firstname')
        roll=request.POST.get('roll')
        dept=request.POST.get('dept')
        city=request.POST.get('city')

        student=StudentModel(
            id=myid,
            ProfilePic=img,
            Name=firstname,
            Roll=roll,
            Department=dept,
            City=city,
        )
        student.save()
        return redirect('student')
    
def viewstudent(request, myid):
    student=StudentModel.objects.filter(id=myid)
    contex={
        'student': student,
    }
    return render(request, 'viewstudent.html',contex)