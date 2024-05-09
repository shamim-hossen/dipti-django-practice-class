from django.shortcuts import redirect,render
from JobApp.models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.hashers import check_password
@login_required
def homepage(requeset):
    return render(requeset, 'homepage.html')

def singin(requeset):
    if requeset.method=='POST':
        username=requeset.POST.get('username')
        password=requeset.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            login(requeset,user)
            return redirect('homepage')
        else:
            return redirect('singin')
    return render(requeset, 'singin.html')

def singup(requeset):
    
    context={
        'success_message':'Account Create Successfully',
        'warning_message':'Password doesn\'t matched',
    }
    if requeset.method=='POST':
        first_name=requeset.POST.get('first_name')
        last_name=requeset.POST.get('last_name')
        username=requeset.POST.get('username')
        password=requeset.POST.get('password')
        confirm_password=requeset.POST.get('confirm_password')
        city=requeset.POST.get('city')
        country=requeset.POST.get('country')
        age=requeset.POST.get('age')
        gender=requeset.POST.get('gender')
        blood=requeset.POST.get('blood')
        user_type=requeset.POST.get('user_type')
        image=requeset.FILES.get('image')
        
        if password==confirm_password:
            user=job_portal_model.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                password=password,
                city=city,
                country=country,
                age=age,
                gender=gender,
                blood=blood,
                user_type=user_type,
                image=image, 
            )
            if user_type == 'recruiter':
                recruiter_model.objects.create(user=user)
                
            elif user_type=='seeker':
                seeker_model.objects.create(user=user)
                basic_information.objects.create(user=user)
                
            
            user.save()
            messages.success(requeset, context['success_message'])
            
            return redirect('singin')
        else:
            messages.warning(requeset, context['warning_message'])
            # return redirect('singup')
        
    return render(requeset, 'singup.html')

def logoutpage(request):
    logout(request)
    return redirect('singin')
@login_required
def addjob(request):
    if request.method=='POST':
        job_type=request.POST.get('job_type')
        workplace=request.POST.get('workplace')
        job_title=request.POST.get('job_title')
        job_description=request.POST.get('job_description')
        job_location=request.POST.get('job_location')
        deadline=request.POST.get('deadline')
        company_logo=request.FILES.get('company_logo')
        requirement=request.POST.get('requirement')
        qualification=request.POST.get('qualification')
        salary=request.POST.get('salary')
        experience=request.POST.get('experience')
        
        file=apply_job(
            job_type=job_type,
            workplace=workplace,
            job_title=job_title,
            job_description=job_description,
            job_location=job_location,
            deadline=deadline,
            company_logo=company_logo,
            requirement=requirement,
            qualification=qualification,
            salary=salary,
            experience=experience,
        )
        if company_logo:
            file.company_logo=company_logo
            file.save()
        return redirect('job_list')
    return render(request, 'addjob.html')
@login_required
def job_list(request):
    jobfile=apply_job.objects.all()
    jobdict={
        'data':jobfile
    }
    return render(request, 'job_list.html', jobdict)

def deletee(request, myid):
    apply_job.objects.get(id=myid).delete()
    return redirect('job_list')

@login_required
def profile(request):
    
    # user1= request.user.user_type
    # if user1 == 'recruiter':
    #    appfile=recruiter_model.objects.filter()
    # elif user1 == 'seeker':
    #     appfile=seeker_model.objects.filter()
    # pdict=(
    #     'data':appfile
    # )
    return render(request, 'profile.html')

@login_required
def editprofile(request):
    current_user=request.user
    if request.method == 'POST':
        gender=request.POST.get('gender')
        blood=request.POST.get('blood')
        age=request.POST.get('age')
        city=request.POST.get('city')
        country=request.POST.get('country')
        # company_logo=request.FILES.get('company_logo')
                    # seeker
        qualification=request.POST.get('qualification')
        experience=request.POST.get('experience')
        skills=request.POST.get('skills')
        certificate=request.POST.get('certificate')
                    # recruiter
        recruiter_name=request.POST.get('recruiter_name')
        company_name=request.POST.get('company_name') 
        company_location=request.POST.get('company_location')
        
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        
        if password == confirm_password:
            
            if check_password(password, current_user.password):
        
                current_user.gender=gender
                current_user.blood=blood
                current_user.age=age
                current_user.city=city
                current_user.country=country
                
                if current_user.user_type == 'seeker':
                    seeker_user = current_user.seekerprofile
                    seeker_user.qualification=qualification
                    seeker_user.experience=experience
                    seeker_user.skills=skills
                    seeker_user.certificate=certificate
                    seeker_user.save()
                    
                elif current_user.user_type == 'recruiter':
                    recuriter_user=current_user.recruiterprofile
                    recuriter_user.recruiter_name=recruiter_name
                    recuriter_user.company_name=company_name
                    recuriter_user.company_location=company_location
                    recuriter_user.save()
                
                current_user.save()
                return redirect("userprofile")

        
    return render(request, 'editprofile.html')

@login_required
def b_information(request):
    return render(request, 'b_information.html')

@login_required
def education_q(request):
    return render(request, 'education_q.html')

@login_required
def work_exp(request):
    return render(request, 'work_exp.html')

@login_required
def con_tact(request):
    return render(request, 'con_tact.html')

@login_required
def userprofile(request):
    return render(request, 'userprofile.html')

def change_passwordPage(request):
    if request.method == 'POST':
        
        current_password=request.POST.get('current_password')
        new_password=request.POST.get('new_password')
        confirm_new_password=request.POST.get('confirm_new_password')
    
        print(current_password,new_password,confirm_new_password)
        
        if check_password(current_password, request.user.password):
            if new_password == confirm_new_password:
                request.user.password=new_password
                request.user.set_password(new_password)
                request.user.save()
                return redirect("userprofile")

    return render(request, 'change_passwordPage.html')