from django.shortcuts import render,redirect
from schoolApp.models import DepartmentAddModel,StudentAddModel

def departmentslist(request):
    Departments=DepartmentAddModel.objects.all()
    Department_Data=[]
    for department in Departments:
        student_count=StudentAddModel.objects.filter(myDepartment=department).count()
        Department_Data.append(
            {
                "Total_Students":student_count,
                "Department_Name":department.Department_Name,
                "HOD":department.Head_of_Department,
                "id":department.id,
            }
        )
    contex={
        'Department_Data':Department_Data
    }

    return render(request,'department/departmentslist.html',contex)

def departmentsadd(request):
    return render(request,'department/departmentsadd.html')

def departmentsedit(request):
    return render(request,'department/departmentsedit.html')

def departmentsdelete(request):
    return redirect('departmentslist')