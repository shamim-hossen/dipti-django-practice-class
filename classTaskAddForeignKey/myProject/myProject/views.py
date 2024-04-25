from django.shortcuts import redirect, render
from myApp.models import CustomUserModel, AddJobModel
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def signUp(request):
    if request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        username=request.POST.get('username')
        propic=request.FILES.get('propic')
        dob=request.POST.get('dob')
        email=request.POST.get('email')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        blood_group=request.POST.get('blood_group')
        user_type=request.POST.get('user_type')
        address=request.POST.get('address')

        if password==cpassword:
            user=CustomUserModel.objects.create_user(
                Fname=fname,
                Lname=lname,
                ProfilePicture=propic,
                DateOfBirth=dob,
                Address=address,
                username=username,
                email=email,
                password=password,

            )
            user.BloodGroup=blood_group
            user.UserType=user_type
            user.save()
            return redirect('signIn')
        else:
            return redirect('signUp')

    return render(request, 'signUp.html')


def signIn(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(
            username=username,
            password=password
        )
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            return redirect('signIn')

    return render(request,'signIn.html')

@login_required
def dashboard(request):
    listjob=AddJobModel.objects.all()
    listjobDict={
        'listjob':listjob,
    }
    return render(request,'dashboard.html', listjobDict)

@login_required
def addJob(request):
    if request.method=='POST':
        job_title=request.POST.get('job_title')
        company_name=request.POST.get('company_name')
        address=request.POST.get('address')
        company_description=request.POST.get('company_description')
        job_description=request.POST.get('job_description')
        qualification=request.POST.get('qualification')
        salary_information=request.POST.get('salary_information')
        deadline=request.POST.get('deadline')
        designation=request.POST.get('designation')
        experience=request.POST.get('experience')
        recruiter=request.user.username

        currentUser=request.user
        currentUsername=request.user.username

        addjob=AddJobModel(
            JobTitle=job_title,
            CompanyName=company_name,
            Address=address,
            CompanyDescription=company_description,
            JobDescription=job_description,
            Qualification=qualification,
            SalaryInformation=salary_information,
            Deadline=deadline,
            Designation=designation,
            Experience=experience,
            OwnerOfJobPost=recruiter,
            Created_by=currentUser,
        )
        addjob.save()
        return redirect('dashboard')
    return render(request, 'addJob.html')

@login_required
def delListJob(request, myid):
    delJob=AddJobModel.objects.get(id=myid)
    delJob.delete()
    return redirect('dashboard')

@login_required
def editJob(request, myid):
    editjob=AddJobModel.objects.filter(id=myid)
    editjobDict={
        'editjob':editjob,
    }
    return render(request, 'editJob.html', editjobDict)

@login_required
def updateJob(request):
    if request.method=='POST':
        myid=request.POST.get('myid')
        job_title=request.POST.get('job_title')
        company_name=request.POST.get('company_name')
        address=request.POST.get('address')
        company_description=request.POST.get('company_description')
        job_description=request.POST.get('job_description')
        qualification=request.POST.get('qualification')
        salary_information=request.POST.get('salary_information')
        deadline=request.POST.get('deadline')
        designation=request.POST.get('designation')
        experience=request.POST.get('experience')
        recruiter=request.user.username

        updateJob=AddJobModel(
            id=myid,
            JobTitle=job_title,
            CompanyName=company_name,
            Address=address,
            CompanyDescription=company_description,
            JobDescription=job_description,
            Qualification=qualification,
            SalaryInformation=salary_information,
            Deadline=deadline,
            Designation=designation,
            Experience=experience,
            OwnerOfJobPost=recruiter,
        )
        updateJob.save()
        return redirect('dashboard')
    
@login_required
def viewJob(request, myid):
    job=AddJobModel.objects.get(id=myid)
    jobDict={
        'job':job,
    }
    return render(request, 'viewJob.html',jobDict)


@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def logOutPage(request):
    logout(request)
    return redirect('signIn')

@login_required
def viewListJob(request):
    print('user:',request.user)#
    print('username:',request.user.username)#
    # listjob=AddJobModel.objects.all()
    # filter(OwnerOfJobPost{
    # shamim123,dipuray123
    #})

    # print(request.user.UserType)
    #jobseeker,recruiter
    if request.user.UserType=='recruiter':
        listjob=AddJobModel.objects.filter(OwnerOfJobPost=request.user.username)
    else:
        listjob=AddJobModel.objects.all()
    listjobDict={
        'listjob':listjob,
    }
    return render(request, 'viewListJob.html', listjobDict)

