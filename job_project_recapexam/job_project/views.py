from django.shortcuts import redirect, render
from job_app.models import CustomUser,AddJobModel
from django.contrib.auth import login, logout,authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        c_password = request.POST.get('c_password')
        role = request.POST.get('role')
        city = request.POST.get('city')
        gender = request.POST.get('gender')
        profile_picture = request.FILES.get('profile_picture')
        email = request.POST.get('email')

        if password == c_password:
            user = CustomUser.objects.create_user(
                username=username,
                password=password,
                role=role,
                city=city,
                gender=gender,
                profile_picture=profile_picture,
                email=email,
            )
            user.save()
            return redirect('signin')

    return render(request, 'signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            username=username,
            password=password,
        )
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'signin.html')

@login_required
def signout(request):
    logout(request)
    return redirect('signin')

@login_required
def home(request):

    return render(request, 'home.html')

def viewalljob(request):
    current_user = request.user
    if current_user.role == "jobseeker":
        job = AddJobModel.objects.all()
    elif current_user.role == "recruiter":
        job = AddJobModel.objects.filter(created_by=current_user)
    contex={
        'job':job
    }
    return render(request, 'viewalljob.html',contex)

@login_required
def profile(request):
    return render(request, 'profile.html')
@login_required
def basicinfo(request):
    
    return render(request, 'basicinfo.html')
@login_required
def cngpass(request):
    if request.method == 'POST':
        cu_password=request.POST.get('cu_password')
        new_password=request.POST.get('new_password')
        con_new_password=request.POST.get('con_new_password')

        if check_password(cu_password, request.user.password):
            if new_password == con_new_password:
                request.user.set_password(new_password)
                request.user.save()
                update_session_auth_hash(request, request.user)
                return redirect('profile')

    return render(request, 'cngpass.html')

@login_required
def addjob(request):
    if request.method == 'POST':
        jobTitle = request.POST.get('jobTitle')
        companyDescription = request.POST.get('companyDescription')
        companyName = request.POST.get('companyName')
        companyLocation = request.POST.get('companyLocation')
        qualifications = request.POST.get('qualifications')
        deadline = request.POST.get('deadline')
        salary = request.POST.get('salary')
        current_user = request.user

        job = AddJobModel(
            jobTitle=jobTitle,
            companyDescription=companyDescription,
            companyName=companyName,
            companyLocation=companyLocation,
            qualifications=qualifications,
            deadline=deadline,
            salary=salary,
            created_by=current_user
        )
        job.save()
        return redirect('viewalljob')


    return render(request, 'recruiter/addjob.html')

@login_required
def deljob(request, myid):
    job = AddJobModel.objects.get(id=myid)
    job.delete()
    return redirect('viewalljob')

@login_required
def editjob(request,myid):
    job = AddJobModel.objects.filter(id = myid)
    jobDict={
        'jobs' : job
    }
    return render(request,'recruiter/editjob.html',jobDict)

@login_required
def updatejob(request):
    if request.method == 'POST':
        myid = request.POST.get('myid')
        jobTitle = request.POST.get('jobTitle')
        companyDescription = request.POST.get('companyDescription')
        companyName = request.POST.get('companyName')
        companyLocation = request.POST.get('companyLocation')
        qualifications = request.POST.get('qualifications')
        deadline = request.POST.get('deadline')
        salary = request.POST.get('salary')
        current_user = request.user

        job = AddJobModel(
            id = myid,
            jobTitle=jobTitle,
            companyName=companyName,
            companyDescription=companyDescription,
            companyLocation=companyLocation,
            qualifications=qualifications,
            deadline=deadline,
            salary=salary,
            created_by=current_user,
        )
        job.save()
        return redirect('viewalljob')
    
@login_required
def seekerinfo(request):
    return render(request,'contactinfo.html')

@login_required
def recruiterinfo(request):
    return render(request,'contactinfo.html')

@login_required
def education(request):
    return render(request,'education.html')

@login_required
def experience(request):
    return render(request,'experience.html')


