from django.shortcuts import redirect, render
from JobApp.models import CustomUserModel,RecruiterModel,SeekerModel,JobModel,JobApplymodel
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.hashers import check_password
from django.contrib.auth import update_session_auth_hash



def signup(request):
    if request.method=="POST":
        username=request.POST.get('username')
        display_name=request.POST.get('display_name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        user_type=request.POST.get('user_type')
        
        if password==confirm_password:
            user = CustomUserModel.objects.create_user(
                username=username,
                display_name=display_name,
                email=email,
                password=password,
                user_type=user_type
            )
            user.save()
            if user_type == 'recruiter':
                RecruiterModel.objects.create(
                    recruiteruser=user
                )
            else:
                SeekerModel.objects.create(
                    seekeruser=user
                )
            return redirect('signin')
    return render(request,'common/registration_page.html')

def signin(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user = authenticate(
            username=username,
            password=password,
        )
        if user:
            login(request,user)
            return redirect('home')
    return render(request,'common/login_page.html')

@login_required
def signout(request):
    logout(request)
    return redirect('signin')

@login_required
def home(request):
    
    return render(request,'common/home.html')

@login_required
def addjob(request):
    if request.method=='POST':
        Title=request.POST.get('Title')
        Number_openings=request.POST.get('Number_openings')
        Category=request.POST.get('Category')
        Job_description=request.POST.get('Job_description')
        Skills=request.POST.get('Skills')

        job=JobModel.objects.create(
            created_by=request.user,
            Title=Title,
            Number_openings=Number_openings,
            Category=Category,
            Job_description=Job_description,
            Skills=Skills,
        )
        job.save()
        return redirect('joblist')
    return render(request,'recruiter/addjob.html')

@login_required
def joblist(request):
    jobs = JobModel.objects.all()
    return render(request,'common/joblist.html',{'jobs':jobs})

@login_required
def deletejob(request,jobid):
    job=JobModel.objects.get(id=jobid)
    job.delete()
    return redirect('joblist')

@login_required
def editjob(request,jobid):
    job=JobModel.objects.get(id=jobid)
    
    if request.method=='POST':
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

@login_required
def viewjob(request,jobid):
    job=JobModel.objects.get(id=jobid)
    return render(request,'common/viewjob.html',{'job':job})

# apply job
@login_required
def applyjob(request,jobid):
    job=JobModel.objects.get(id=jobid)
    
    if request.method=='POST':
        skills=request.POST.get('skills')
        resume=request.FILES.get('resume')
        
        applyjob=JobApplymodel.objects.create(
            skills=skills,
            resume=resume,
            applicant=request.user,
            applied_job=job,
        )
        applyjob.save()
        return redirect('joblist')
    return render(request,'seeker/applyjob.html',{'job':job})


@login_required
def jobsearch(request):
    jobs = []
    if request.method == 'GET':
        skills = request.GET.get('skills')
        if skills:
            jobs = JobModel.objects.filter(
                Q(Skills__icontains=skills)
            )
    return render(request, 'common/searchjob.html', {'jobs': jobs})


@login_required
def profile(request):
    return render(request,'profile/profile.html')

@login_required
def basicinfo(request):
    return render(request,'profile/basicinfo.html')

@login_required
def seekerinfo(request):
    return render(request,'profile/seekerinfo.html')

@login_required
def recruiterinfo(request):
    return render(request,'profile/recruiterinfo.html')

@login_required
def changepassword(request):
    if request.method=="POST":
        current_password=request.POST.get('current_password')
        new_password=request.POST.get('new_password')
        new_con_password=request.POST.get('new_con_password')

        pass_check=check_password(current_password,request.user.password)
        if pass_check:
            if new_password == new_con_password:
                request.user.set_password(new_password)
                request.user.save()
                update_session_auth_hash(request,request.user)
                return redirect('home')
    return render(request,'common/changepassword.html')

@login_required
def editbasicinfo(request):
    if request.method=='POST':
        display_name=request.POST.get('display_name')
        
        user_cus=CustomUserModel.objects.get(username=request.user)
        user_cus.display_name=display_name

        user_cus.save()
        return redirect('basicinfo')
    return render(request,'profile/editbasicinfo.html')

@login_required
def editseekerprofile(request):
    if request.method =="POST":
        Skills=request.POST.get('Skills')
        Resume=request.FILES.get('Resume')
        
        seeker = SeekerModel.objects.get(seekeruser=request.user)
        seeker.Skills=Skills
        seeker.Resume=Resume
        seeker.save()
        return redirect('seekerinfo')
    return render(request,'profile/editseekerprofile.html')

@login_required
def editrecruiterprofile(request):
    if request.method =="POST":
        company_name=request.POST.get('company_name')
        company_address=request.POST.get('company_address')
        
        recruiter = RecruiterModel.objects.get(recruiteruser=request.user)
        recruiter.company_name=company_name
        recruiter.company_address=company_address
        recruiter.save()
        return redirect('recruiterinfo')
    return render(request,'profile/editrecruiterprofile.html')



@login_required
def appliedjob(request):
    current_user = request.user
    applied_job = JobApplymodel.objects.filter(applicant=current_user)
    no_applied_jobs = False
    
    if not applied_job:
        no_applied_jobs = True

    return render(request, 'seeker/appliedjob.html', {'applied_job': applied_job, 'no_applied_jobs': no_applied_jobs})

# jobs=JobModel.objects.filter(skill=search input name)