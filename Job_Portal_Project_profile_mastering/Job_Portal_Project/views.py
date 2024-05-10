from django.shortcuts import redirect, render
from JobApp.models import CustomUserModel, AddJobModel,RecruiterContactInfo,RecruiterProfileModel,SeekerProfileModel,SeekerBasicInfoModel,SeekerEducationQualificationModel,SeekerWorkExperienceModel,SeekerContentModel
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.contrib.auth import update_session_auth_hash

def signup(request):
    if request.method=='POST':
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        blood_group=request.POST.get('blood_group')
        user_type=request.POST.get('user_type')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        city=request.POST.get('city')
        country=request.POST.get('country')
        username=request.POST.get('username')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        profile_photo=request.FILES.get('profile_photo')

        if password==confirm_password:
            user=CustomUserModel.objects.create_user(
                Age=age,
                Gender=gender,
                BloodGroup=blood_group,
                UserType=user_type,
                first_name=first_name,
                last_name=last_name,
                City=city,
                Country=country,
                username=username,
                password=confirm_password,
                Profile_photo=profile_photo,
            )

            if user_type == 'jobrecruiter':
                AddJobModel.objects.create(user=user)
                RecruiterProfileModel.objects.create(user=user)
                RecruiterContactInfo.objects.create(user=user)
            elif user_type == 'jobseeker':
                SeekerProfileModel.objects.create(user=user)
                SeekerBasicInfoModel.objects.create(user=user)
                SeekerEducationQualificationModel.objects.create(user=user)
                SeekerWorkExperienceModel.objects.create(user=user)
                SeekerContentModel.objects.create(user=user)
            user.save()
            return redirect('signin')
        else:
            return redirect('signup')
    return render(request, 'signup.html')

def signin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(
            username=username,
            password=password,
        )
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            return redirect('signin')

    return render(request, 'signin.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def logoutfn(request):
    logout(request)
    return redirect('signin')

@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def addjob(request):
    if request.method=='POST':
        job_title=request.POST.get('job_title')
        job_description=request.POST.get('job_description')
        job_location=request.POST.get('job_location')
        deadline=request.POST.get('deadline')
        company_logo=request.FILES.get('company_logo')
        requirements=request.POST.get('requirements')
        qualification=request.POST.get('qualification')
        job_type=request.POST.get('job_type')
        workplace=request.POST.get('workplace')
        salary=request.POST.get('salary')
        experience=request.POST.get('experience')

        job=AddJobModel(
            JobTitle=job_title,
            JobDescription=job_description,
            JobLocation=job_location,
            Deadline=deadline,
            CompanyLogo=company_logo,
            Requirements=requirements,
            Qualification=qualification,
            JobType=job_type,
            Workplace=workplace,
            Salary=salary,
            Experience=experience,
            Created_By=request.user,
        )
        job.save()
        return redirect('viewalljob')
    return render(request, 'addjob.html')

@login_required
def editjob(request, myid):
    job=AddJobModel.objects.get(id=myid)
    contex={
        'job': job,
    }
    return render(request, 'editjob.html', contex)

@login_required
def updatejob(request):
    if request.method=='POST':
        myid=request.POST.get('myid')
        job_title=request.POST.get('job_title')
        job_description=request.POST.get('job_description')
        job_location=request.POST.get('job_location')
        deadline=request.POST.get('deadline')
        company_logo=request.FILES.get('company_logo')
        requirements=request.POST.get('requirements')
        qualification=request.POST.get('qualification')
        job_type=request.POST.get('job_type')
        workplace=request.POST.get('workplace')
        salary=request.POST.get('salary')
        experience=request.POST.get('experience')

        if company_logo:
            job=AddJobModel(
                id=myid,
                JobTitle=job_title,
                JobDescription=job_description,
                JobLocation=job_location,
                Deadline=deadline,
                CompanyLogo=company_logo,
                Requirements=requirements,
                Qualification=qualification,
                JobType=job_type,
                Workplace=workplace,
                Salary=salary,
                Experience=experience,
                Created_By=request.user,
            )
        else:
            byid=AddJobModel.objects.get(id=myid)
            job=AddJobModel(
                id=myid,
                JobTitle=job_title,
                JobDescription=job_description,
                JobLocation=job_location,
                Deadline=deadline,
                CompanyLogo=byid.CompanyLogo,
                Requirements=requirements,
                Qualification=qualification,
                JobType=job_type,
                Workplace=workplace,
                Salary=salary,
                Experience=experience,
                Created_By=request.user,
            )
        job.save()
    return redirect('viewalljob')

@login_required
def deljob(request,myid):
    job=AddJobModel.objects.get(id=myid)
    job.delete()
    return redirect('viewalljob')

@login_required
def viewjob(request, myid):
    job=AddJobModel.objects.get(id=myid)
    contex={
        'job': job,
    }
    return render(request, 'viewjob.html',contex)

@login_required
def viewalljob(request):
    currentuser=request.user
    if currentuser.UserType == 'jobrecruiter':
        job=AddJobModel.objects.filter(Created_By=currentuser)
    else:
        job=AddJobModel.objects.all()
    contex={
        'job': job,
    }
    return render(request, 'viewalljob.html',contex)


def appliedjob(request):
    return render(request, 'appliedjob.html')

def postedjob(request):
    currentuser=request.user
    job=AddJobModel.objects.filter(Created_By=currentuser)
    contex={
        'job':job,
    }
    return render(request, 'postedjob.html', contex)

def editprofile(request):
    return render(request, 'editprofile.html')

def profilebasicinfo(request):
    return render(request, 'profilecontent.html')

def profilerecruitercontact(request):
    return render(request, 'profilerecruitercontact.html')

def educationqualification(request):
    return render(request, 'educationqualification.html')

def workexperience(request):
    return render(request, 'workexperience.html')

def content(request):
    return render(request, 'content.html')

def change_pass(request):
    if request.method=='POST':
        current_password=request.POST.get('current_password')
        new_password=request.POST.get('new_password')
        confirm_password=request.POST.get('confirm_password')

        if check_password(current_password, request.user.password):
            if new_password==confirm_password:
                request.user.set_password(new_password)
                request.user.save()
                update_session_auth_hash(request, request.user)
                return redirect('profile')
    return render(request, 'changepass.html')