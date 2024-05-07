from django.shortcuts import render, redirect
from JobApp.models import*
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.

def signup(request):
    if request.method=='POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        blood_group=request.POST.get('blood_group')
        city=request.POST.get('city')
        country=request.POST.get('country')
        user_type=request.POST.get('user_type')
        photo=request.FILES.get('photo')

        if password==confirm_password:
            user=custom_user.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                password=password,
                age=age,
                gender=gender,
                blood_group=blood_group,
                city=city,
                country=country,
                user_type=user_type,
                photo=photo,
            )
            user.save()
            basic_info(user=user).save()
            contact(user=user).save()
            if user_type=='recruiter':
                job_recruiter_profile(user=user).save()

            else:
                job_seeker_profile(user=user).save()
                education(user=user).save()
                experience(user=user).save()
            
            
            return redirect('signin')

    return render(request,'signup.html')

def signin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('deshboard')

    return render(request,'signin.html')

def signout(request):
    logout(request)
    return redirect('signin')

@login_required
def deshboard(request):
    if request.user.user_type=='recruiter':
        data=addjobModel.objects.filter(create_by=request.user)
        return render(request, 'deshboard.html',{'data':data})
    else:
        data=addjobModel.objects.all()
        return render(request, 'deshboard.html',{'data':data})

@login_required
def addjob(request):
    if request.method=='POST':
        job_title=request.POST.get('job_title')
        job_description=request.POST.get('job_description')
        job_location=request.POST.get('job_location')
        deadline=request.POST.get('deadline')
        requirments=request.POST.get('requirments')
        company_logo=request.FILES.get('company_logo')
        qualification=request.POST.get('qualification')
        job_type=request.POST.get('job_type')
        work_place=request.POST.get('work_place')
        salary=request.POST.get('salary')
        experience=request.POST.get('experience')
        create_by=custom_user.objects.get(id=request.user.id)

        newJob=addjobModel(
            job_title=job_title,
            job_description=job_description,
            job_location=job_location,
            deadline=deadline,
            requirments=requirments,
            company_logo=company_logo,
            qualification=qualification,
            job_type=job_type,
            work_place=work_place,
            salary=salary,
            experience=experience,
            create_by=create_by,
        )
        newJob.save()
        return redirect('deshboard')


    return render(request, 'addjob.html')

@login_required
def jobdelete(request, id):
    addjobModel.objects.get(id=id).delete()
    return redirect('deshboard')

@login_required
def viewjob(request,id):
    view=addjobModel.objects.get(id=id)
    return render(request, 'viewjob.html',{'view':view})

@login_required
def editjob(request,id):
    edit=addjobModel.objects.get(id=id)
    if request.method=='POST':
        id=request.POST.get('id')
        job_title=request.POST.get('job_title')
        job_description=request.POST.get('job_description')
        job_location=request.POST.get('job_location')
        deadline=request.POST.get('deadline')
        requirments=request.POST.get('requirments')
        company_logo=request.FILES.get('company_logo')
        company_logo1=request.POST.get('company_logo1')
        qualification=request.POST.get('qualification')
        job_type=request.POST.get('job_type')
        work_place=request.POST.get('work_place')
        salary=request.POST.get('salary')
        experience=request.POST.get('experience')

        newJob=addjobModel(
            id=id,
            job_title=job_title,
            job_description=job_description,
            job_location=job_location,
            deadline=deadline,
            requirments=requirments,
            qualification=qualification,
            job_type=job_type,
            work_place=work_place,
            salary=salary,
            experience=experience,
        )
        if company_logo:
            newJob.company_logo=company_logo
        else:
            newJob.company_logo=company_logo1

        newJob.save()
        return redirect('deshboard')

    return render(request, 'editjob.html',{'edit':edit})

@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def editprofile(request):
    return render(request, 'editprofile.html')

@login_required
def basic_info(request):
    return render(request, 'basic_info.html')

@login_required
def education(request):
    return render(request, 'education.html')

@login_required
def contact(request):
    return render(request, 'contact.html')

@login_required
def experience(request):
    return render(request, 'experience.html')