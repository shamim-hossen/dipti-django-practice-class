from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from django.contrib.auth import update_session_auth_hash
from schoolApp.models import *

def studentdashboard(request):
    return render(request,'student/studentdashboard.html')

def studentlist(request):
    student=StudentAddModel.objects.all()
    stDict={
        'student':student
    }
    return render(request,'student/studentlist.html',stDict)

def studentadd(request):
    department =DepartmentAddModel.objects.all()
    sessions =SessionAddModel.objects.all()
    dept_sessDict={
        'department':department,
        'sessions':sessions,
    }
    if request.method=="POST":
        First_Name=request.POST.get('First_Name')
        Last_Name=request.POST.get('Last_Name')
        Email=request.POST.get('Email')
        Student_Id=request.POST.get('Student_Id')
        Gender=request.POST.get('Gender')
        Section=request.POST.get('Section')
        Date_of_Birth=request.POST.get('Date_of_Birth')
        Department_Name=request.POST.get('Department_Name')
        Religion=request.POST.get('Religion')
        Mobile_Number=request.POST.get('Mobile_Number')
        Session_Year=request.POST.get('Session_Year')
        Student_Image=request.FILES.get('Student_Image')
        Father_Name=request.POST.get('Father_Name')
        Father_Occupation=request.POST.get('Father_Occupation')
        Father_Mobile=request.POST.get('Father_Mobile')
        Father_Email=request.POST.get('Father_Email')
        Mother_Name=request.POST.get('Mother_Name')
        Mother_Occupation=request.POST.get('Mother_Occupation')
        Mother_Mobile=request.POST.get('Mother_Mobile')
        Mother_Email=request.POST.get('Mother_Email')
        Present_Address=request.POST.get('Present_Address')
        Permanent_Address=request.POST.get('Permanent_Address')
        Username=request.POST.get('Username')
        Password=request.POST.get('Password')
        CPassword=request.POST.get('CPassword')
        
        student_custom=CustomUserModel.objects.create_user(
            username=Username,
            password=Password,
            user_type="3"
        )
        student_custom.save()
        if Password==CPassword:
            student=StudentAddModel.objects.create(
            user=student_custom,
            First_Name=First_Name,
            Last_Name=Last_Name,
            Email=Email,
            Student_Id=Student_Id,
            Gender=Gender,
            Section=Section,
            Date_of_Birth=Date_of_Birth,
            Department_Name=Department_Name,
            Religion=Religion,
            Mobile_Number=Mobile_Number,
            Session_Year=Session_Year,
            Student_Image=Student_Image,
            Father_Name=Father_Name,
            Father_Occupation=Father_Occupation,
            Father_Mobile=Father_Mobile,
            Father_Email=Father_Email,
            Mother_Name=Mother_Name,
            Mother_Occupation=Mother_Occupation,
            Mother_Mobile=Mother_Mobile,
            Mother_Email=Mother_Email,
            Present_Address=Present_Address,
            Permanent_Address=Permanent_Address,
            )
            student.save()
            return redirect('studentlist')
    return render(request,'student/studentadd.html',dept_sessDict)

def studentdetails(request,stuid):
    student_data=StudentAddModel.objects.get(id=stuid)
    stuDict={
        'student_data':student_data,

    }
    return render(request,'student/studentdetails.html',stuDict)

def studentedit(request,stuid):
    
    department =DepartmentAddModel.objects.all()
    sessions =SessionAddModel.objects.all()
    student_data=StudentAddModel.objects.get(id=stuid)
    stuDict={
        'student_data':student_data,
        'department':department,
        'sessions':sessions,
    }
    if request.method=="POST":
        First_Name=request.POST.get('First_Name')
        Last_Name=request.POST.get('Last_Name')
        Email=request.POST.get('Email')
        Student_Id=request.POST.get('Student_Id')
        Gender=request.POST.get('Gender')
        Section=request.POST.get('Section')
        Date_of_Birth=request.POST.get('Date_of_Birth')
        Department_Name=request.POST.get('Department_Name')
        Religion=request.POST.get('Religion')
        Mobile_Number=request.POST.get('Mobile_Number')
        Session_Year=request.POST.get('Session_Year')
        Student_Image=request.FILES.get('Student_Image')
        Father_Name=request.POST.get('Father_Name')
        Father_Occupation=request.POST.get('Father_Occupation')
        Father_Mobile=request.POST.get('Father_Mobile')
        Father_Email=request.POST.get('Father_Email')
        Mother_Name=request.POST.get('Mother_Name')
        Mother_Occupation=request.POST.get('Mother_Occupation')
        Mother_Mobile=request.POST.get('Mother_Mobile')
        Mother_Email=request.POST.get('Mother_Email')
        Present_Address=request.POST.get('Present_Address')
        Permanent_Address=request.POST.get('Permanent_Address')
        Username=request.POST.get('Username')
        Password=request.POST.get('CPassword')
        CPassword=request.POST.get('CPassword')

        # current user info 
        user = CustomUserModel.objects.get(username=Username)
        user_password = user.password
        user_auth =check_password(CPassword,user_password)
        if user_auth:
            if Password==CPassword:
                StudentAddModel.objects.filter(id=stuid).update(
                    First_Name=First_Name,
                    Last_Name=Last_Name,
                    Email=Email,
                    Student_Id=Student_Id,
                    Gender=Gender,
                    Section=Section,
                    Date_of_Birth=Date_of_Birth,
                    Department_Name=Department_Name,
                    Religion=Religion,
                    Mobile_Number=Mobile_Number,
                    Session_Year=Session_Year,
                    Student_Image=Student_Image,
                    Father_Name=Father_Name,
                    Father_Occupation=Father_Occupation,
                    Father_Mobile=Father_Mobile,
                    Father_Email=Father_Email,
                    Mother_Name=Mother_Name,
                    Mother_Occupation=Mother_Occupation,
                    Mother_Mobile=Mother_Mobile,
                    Mother_Email=Mother_Email,
                    Present_Address=Present_Address,
                    Permanent_Address=Permanent_Address,
                    )
                return redirect('studentlist')
    return render(request,'student/studentedit.html',stuDict)

def studentadelete(request,stuid):
    custom_student=CustomUserModel.objects.get(username=stuid)
    custom_student.delete()
    return redirect('studentlist')

