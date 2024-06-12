from django.shortcuts import redirect, render,get_object_or_404
from Shamim_06_JobPortal.forms import *
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method=='POST':
        form=CustomUserForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.save()
            if user.user_type == 'recruiter':
                user = RecruiterModel.objects.create(user=user)
            else:
                user = SeekerModel.objects.create(user=user)
            return redirect('signin')
    else:
        form=CustomUserForm()
    return render(request, 'common/signup.html',{'form':form})


def signin(request):
    if request.method=='POST':
        form=CustomUserAuthForm(request,data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('home')
    else:
        form=CustomUserAuthForm()
    return render(request, 'common/signin.html')


@login_required
def signout(request):
    logout(request)
    return redirect('signin')


@login_required
def home(request):

    return render(request,'common/home.html')


@login_required
def profile(request):

    return render(request,'profile/profile.html')


@login_required
def addjob(request):
    if request.method=='POST':
        current_user=request.user
        form=JobForm(request.POST)
        if form.is_valid():
            form=form.save(commit=False)
            form.created_by=current_user
            form.save()
            return redirect('joblist')
    else:
        form=JobForm()
    return render(request, 'recruiter/addjob.html',{'form':form})


@login_required
def joblist(request):
    jobs=JobModel.objects.all()
    return render(request,'seeker/joblist.html',{'jobs':jobs})


@login_required
def deletejob(request,jobid):
    job=get_object_or_404(JobModel,id=jobid)
    job.delete()
    return redirect('joblist')


@login_required
def editjob(request,jobid):
    job=get_object_or_404(JobModel,id=jobid)
    print("I am outside of POST")
    if request.method=='POST':
        print("I am inside of POST")
        form=JobForm(request.POST,instance=job)
        if form.is_valid():
            form.save()
            return redirect('joblist')
    else:
        form=JobForm(instance=job)
    return render(request,'recruiter/editjob.html',{'form':form})


@login_required
def applyjob(request,jobid):
    # job=get_object_or_404(JobModel,id=jobid)
    # if request.method=='POST':
    #     current_user=request.user
    #     form=JobApplyForm(request.POST,request.FILES)
    #     if form.is_valid():
    #         form=form.save(commit=False)
    #         form.user=current_user
    #         form.applied_job=job
    #         form.save()
    #         return redirect('joblist')
    # else:
    #     form=JobApplyForm()
    jobs=JobApplyModel.objects.filter(user=request.user)
    return render(request,'seeker/applyjob.html',{'jobs':jobs})

def postedjob(request):
    # jobs=JobModel.objects.filter(user=request.user)
    return render(request,'recruiter/postedjob.html')


@login_required
def skillset(request):
    current_user = request.user
    seeker_instance = get_object_or_404(SeekerModel, user=current_user)
    
    if request.method == 'POST':
        form = SeekerForm(request.POST, instance=seeker_instance)
        if form.is_valid():
            form.save()
            return redirect('profile')  
    else:
        form = SeekerForm()
    return render(request,'profile/skillsets.html',{'form': form})


@login_required
def companyinfo(request):
    current_user = request.user
    recruiter_instance = get_object_or_404(RecruiterModel, user=current_user)
    
    if request.method == 'POST':
        form = RecruiterForm(request.POST, instance=recruiter_instance)
        if form.is_valid():
            form.save()
            return redirect('profile') 
    else:
        form = RecruiterForm()
    return render(request,'profile/companyinfo.html',{'form': form})


@login_required
def basicinfo(request):
    user = request.user
    return render(request,'profile/basicinfo.html',{'user':user})

def accept(request,id):
	apply=JobApplyModel.objects.get(id=id)
	apply.status='Accepted'
	apply.save()
	return redirect('applicant_list',id=apply.job.id)