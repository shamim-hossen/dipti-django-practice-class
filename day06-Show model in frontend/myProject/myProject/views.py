from django.shortcuts import render
from myApp.models import StudentModel
def studentPage(request):
    student=StudentModel.objects.all()
    stuDict={
        'student':student
    }
    return render(request, 'studentPage.html', stuDict)