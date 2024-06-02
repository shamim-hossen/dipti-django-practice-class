from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from job_app.models import CustomUser, AddJobModel
from django.contrib.auth.hashers import check_password
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

all_message = {
    "signup_success":"Successfully signed up",
    "signup_warning":"not signup",
    "addjob_success":"Successfully add job",
    "signin_success":"Successfully signed in",
}

def signup(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        gender=request.POST.get('gender')
        user_type=request.POST.get('user_type')
        profile_picture=request.FILES.get('profile_picture')

        if password == confirm_password:
            user = CustomUser.objects.create_user(
                username=username,
                password=password,
                gender=gender,
                user_type=user_type,
                profile_picture=profile_picture,
            )
            user.save()
            messages.success(request, all_message['signup_success'])
            return redirect('signin')
        else:
            messages.warning(request, all_message['signup_warning'])
            return redirect('signup')
    return render(request, 'common/signup.html')


def signin(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user = authenticate(
            username = username,
            password = password
        )
        if user:
            login(request, user)
            messages.success(request, all_message['signin_success'])
            return redirect('home')
    return render(request, 'common/signin.html')

@login_required
def signout(request):
    logout(request)
    return redirect('home')

@login_required
def home(request):
    
    return render(request, 'home.html')

def profile(request):
    
    return render(request, 'profile.html')

def cngpassword(request):
    if request.method == 'POST':
        cu_password = request.POST.get('cu_password')
        new_password = request.POST.get('new_password')
        con_new_password = request.POST.get('con_new_password')
        
        if check_password(cu_password, request.user.password):
            if new_password == con_new_password:
                request.user.set_password(new_password)
                request.user.save()
                update_session_auth_hash(request, request.user)
                return redirect('profile')
    return render(request, 'cngpass.html')
def basicinfo(request):

    return render(request, 'basicinfo.html')
def addjob(request):
    if request.method == 'POST':
        job_title = request.POST.get('job_title')
        company_name = request.POST.get('company_name')
        address = request.POST.get('address')
        company_description = request.POST.get('company_description')
        job_description = request.POST.get('job_description')
        qualification = request.POST.get('qualification')
        salary_information = request.POST.get('salary_information')
        deadline = request.POST.get('deadline')
        designation = request.POST.get('designation')
        experience = request.POST.get('experience')
        current_user = request.user

        addjob = AddJobModel(
            job_title=job_title,
            company_name=company_name,
            address=address,
            company_description=company_description,
            job_description=job_description,
            qualification=qualification,
            salary_information=salary_information,
            deadline=deadline,
            designation=designation,
            experience=experience,
            created_by=current_user
        )
        addjob.save()
        messages.success(request, all_message['addjob_success'])
        return redirect('home')

    return render(request, 'recruiter/addjob.html')


def viewalljob(request):
    job = AddJobModel.objects.all()
    contex = {
        'job': job,
    }
    return render(request, 'viewalljob.html',contex)
