from django.shortcuts import redirect,render
from jobApp.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == 'POST':
        display_name = request.POST.get('display_name')
        profile_picture = request.FILES.get('profile_picture')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        user_type = request.POST.get('user_type')

        if password == confirm_password:
            user = CustomUser.objects.create_user(
                display_name=display_name,
                profile_picture=profile_picture,
                username=username,
                password=password,
                user_type=user_type
            )
            user.save()

            if user_type == 'recruiter':
                RecruiterModel.objects.create(recruiteruser=user)
            else:
                SeekerModel.objects.create(seekeruser=user)

            return redirect('signin')
    return render(request, 'common/signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            username = username,
            password = password
        )
        if user:
            login(request,user)
            return redirect('home')
    return render(request, 'common/signin.html')
@login_required
def signout(request):
    logout(request)
    return redirect('signin')

@login_required
def home(request):
    return render(request, 'common/home.html')

@login_required
def joblist(request):
    jobs=JobModel.objects.all()
    return render(request, 'common/joblist.html',{'jobs':jobs})


def addjob(request):
    if request.method=='POST':
        Title=request.POST.get('Title')
        Number_openings=request.POST.get('Number_openings')
        Category=request.POST.get('Category')
        Job_description=request.POST.get('Job_description')
        Skills=request.POST.get('Skills')

        job=JobModel.objects.create(
            Title=Title,
            Number_openings=Number_openings,
            Category=Category,
            Job_description=Job_description,
            Skills=Skills,
            created_by=request.user
        )
        job.save()
        return redirect('joblist')
    return render(request, 'recruiter/addjob.html')

def deletejob(request, jobid):
    job=JobModel.objects.get(id=jobid)
    job.delete()
    return redirect('joblist')


def editjob(request, jobid):
    job=JobModel.objects.get(id=jobid)

    if request.method == 'POST':
        Title=request.POST.get('Title')
        Number_openings=request.POST.get('Number_openings')
        Category=request.POST.get('Category')
        Job_description=request.POST.get('Job_description')
        Skills=request.POST.get('Skills')
        
        job=JobModel.objects.get(id=jobid)
        job.Title=Title
        job.Number_openings=Number_openings
        job.Category=Category
        job.Job_description=Job_description
        job.Skills=Skills
        job.save()
        return redirect('joblist')
    return render(request,'recruiter/editjob.html',{'job':job})