from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from jobApp.models import CustomUserModel,RecruiterProfileModel,SeekerProfileModel,SeekerEducationModel,SeekerWorkExModel,BasicInfoModel,ContactModel,AddJobModel
import re
all_messages ={
    "signup_success":"Successfully signed up",
    "signin_success":"Successfully signed in",
    "name_warning":"Name can only contain letters",
    "username_warning":"username can only contain letters and number",
    "username_warning2":"Username Already exists",
    "password_warning":"Password and confirm password not matched!",
    "age_warning":"You need to be 18 Years or above",
    "signin_warning":"Credentials not match",
    "username_warning3":"Username does not exists",
    "addjob_success":"Job added successfully",
    "editjob_success":"Job updated successfully",
    "logout_success":"Log out successful",
    "password_change_success":"Password change successful",
    "password_change_warning1":"New and confirm password not matched!",
    "password_change_warning2":"Current password not matched with database password!",
}

def signup(request):
    if request.method == "POST":
        profilePhoto = request.FILES.get('profilePhoto')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirmPassword')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        city = request.POST.get('city')
        country = request.POST.get('country')
        bloodGroup = request.POST.get('bloodGroup')
        userType = request.POST.get('userType')
        
        # Preserve data
        context={
            'first_name':first_name,
            'last_name':last_name,
            'username':username,
            'password':password,
            'confirmPassword':confirmPassword,
            'age':age,
            'gender':gender,
            'city':city,
            'country':country,
            'bloodGroup':bloodGroup,
            'userType':userType,
        }
        # checking name
        def name_check(*names):
            for name in names:
                if not re.match(r"^[a-zA-Z\s]+$", name):
                    return False
            return True
        
        # checking username
        def username_check(username):
            existing_user = CustomUserModel.objects.filter(username=username).exists()
            if existing_user:
                return True
            
        # checking age
        def age_check(age):
            age=int(age)
            if 18<=age<=100:
                return True
        
        # checking city,country name
        def country_city_check(*names):
            for name in names:
                if not re.match(r"^[a-zA-Z]+$", name):
                    return False
            return True

        if not name_check(first_name,last_name):
            messages.warning(request,all_messages['name_warning'])
            return render(request,'signup.html',context)
        if username_check(username):
            messages.warning(request,all_messages['username_warning2'])
            return render(request,'signup.html',context)
        if not age_check(age):
            messages.warning(request,all_messages['age_warning'])
            return render(request,'signup.html',context)
        if not country_city_check(city,country):
            messages.warning(request,all_messages['name_warning'])
            return render(request,'signup.html',context)
        if password==confirmPassword:
            user = CustomUserModel.objects.create_user(
                profilePhoto=profilePhoto,
                first_name=first_name,
                last_name=last_name,
                username=username,
                password=password,
                age=age,
                gender=gender,
                city=city,
                country=country,
                bloodGroup=bloodGroup,
                userType=userType,
            )
            if user.userType=='recruiter':
                RecruiterProfileModel.objects.create(user=user)
            elif user.userType=='seeker':
                SeekerProfileModel.objects.create(user=user)
                SeekerEducationModel.objects.create(user=user)
                SeekerWorkExModel.objects.create(user=user)

            BasicInfoModel.objects.create(user=user)
            ContactModel.objects.create(user=user)
            user.save()
            messages.success(request,all_messages['signup_success'])
            return redirect('signin')
        else:
            messages.warning(request,all_messages['password_warning'])
            return render(request,"signup.html",context)
    return render(request,"signup.html")

def signin(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        context ={
            'username':username,
            'password':password,
        }
        user = authenticate(
            username=username,
            password=password
        )
        existing_user = CustomUserModel.objects.filter(username=username).exists()
        if not existing_user:
            messages.warning(request,all_messages['username_warning3'])
            return render(request,'signin.html',context)
        if user:
            login(request,user)
            messages.success(request,all_messages['signin_success'])
            return redirect('dashboard')
        if not user:
            messages.warning(request,all_messages['signin_warning'])
            return render(request,'signin.html',context)
    return render(request,'signin.html')

@login_required
def dashboard(request):
    current_user = request.user
    if current_user.userType == "seeker":
        job = AddJobModel.objects.all()
    elif current_user.userType == "recruiter":
        job = AddJobModel.objects.filter(created_by=current_user)
    jobDict={
        'job':job
    }
    return render(request,'dashboard.html',jobDict)

def logoutpage(request):
    logout(request)
    messages.success(request,all_messages['logout_success'])
    return redirect('signin')

@login_required
def profile(request):
    return render(request,'profile.html')

@login_required
def profileinfo(request):
    return render(request,'profileinfo.html')

@login_required
def recruiterprofile(request):
    return render(request,'recruiter/recruiterprofile.html')

@login_required
def seekerprofile(request):
    return render(request,'seeker/seekerprofile.html')

@login_required
def seekereducation(request):
    return render(request,'seeker/seekereducation.html')

@login_required
def seekerworkex(request):
    return render(request,'seeker/seekerworkex.html')

@login_required
def basicinfo(request):
    return render(request,'basicinfo.html')

@login_required
def contactinfo(request):
    return render(request,'contactinfo.html')

@login_required
def editprofile(request):
    if request.method == "POST":
        profile_photo = request.FILES.get("profile_photo")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        age = request.POST.get("age")
        gender = request.POST.get("gender")
        country = request.POST.get("country")
        bloodGroup = request.POST.get("bloodGroup")
        userType = request.POST.get("userType")
        father_name = request.POST.get("father_name")
        mother_name = request.POST.get("mother_name")
        hobby = request.POST.get("hobby")
        languages = request.POST.get("languages")
        mobile_number = request.POST.get("mobile_number")
        email = request.POST.get("email")
        address = request.POST.get("address")
        qualification = request.POST.get("qualification")
        experience = request.POST.get("experience")
        skills = request.POST.get("skills")
        last_education = request.POST.get("last_education")
        education_name = request.POST.get("education_name")
        education_year = request.POST.get("education_year")
        education_institute = request.POST.get("education_institute")
        Position = request.POST.get("Position")
        Company_name = request.POST.get("Company_name")
        Duration = request.POST.get("Duration")
        company_name = request.POST.get("company_name")
        company_location = request.POST.get("company_location")
        recruiter_name = request.POST.get("recruiter_name")
        password = request.POST.get("password")
        cpassword = request.POST.get("cpassword")
        current_user = request.user
        if password == cpassword:
            if check_password(cpassword,current_user.password):
                current_user.profile_photo = profile_photo
                current_user.first_name = first_name
                current_user.last_name = last_name
                current_user.age = age
                current_user.gender = gender
                current_user.country = country
                current_user.bloodGroup = bloodGroup
                current_user.save()
                current_user.basicinfomodel.father_name = father_name
                current_user.basicinfomodel.mother_name = mother_name
                current_user.basicinfomodel.hobby = hobby
                current_user.basicinfomodel.languages = languages
                current_user.basicinfomodel.save()
                current_user.contactmodel.mobile_number = mobile_number
                current_user.contactmodel.email = email
                current_user.contactmodel.address = address
                current_user.contactmodel.save()
                if current_user.userType == "seeker":
                    current_user.seekerprofilemodel.Qualification = qualification
                    current_user.seekerprofilemodel.Experience = experience
                    current_user.seekerprofilemodel.Skills = skills
                    current_user.seekerprofilemodel.last_education = last_education
                    current_user.seekerprofilemodel.save()
                    current_user.seekereducationmodel.education_name = education_name
                    current_user.seekereducationmodel.education_year = education_year
                    current_user.seekereducationmodel.education_institute = education_institute
                    current_user.seekereducationmodel.save()
                    current_user.seekerworkexmodel.Position = Position
                    current_user.seekerworkexmodel.Company_name = Company_name
                    current_user.seekerworkexmodel.Duration = Duration
                    current_user.seekerworkexmodel.save()
                elif current_user.userType == "recruiter":
                    current_user.recruiterprofilemodel.Company_name = company_name
                    current_user.recruiterprofilemodel.Company_location = company_location
                    current_user.recruiterprofilemodel.Recruiter_Name = recruiter_name
                    current_user.recruiterprofilemodel.save()
                return redirect('profile')
    return render(request,'editprofile.html')

@login_required
def changepassword(request):
    if request.method == "POST":
        cu_password=request.POST.get('cu_password')
        new_password=request.POST.get('new_password')
        con_new_password=request.POST.get('con_new_password')
        
        # preserve data
        context={
            'cu_password':cu_password,
            'new_password':new_password,
            'con_new_password':con_new_password,
        }
        if check_password(cu_password,request.user.password):
            if new_password == con_new_password:
                request.user.set_password(new_password)
                request.user.save()
                update_session_auth_hash(request,request.user)
                messages.success(request,all_messages['password_change_success'])
                return redirect('profile')
            else:
                messages.warning(request,all_messages['password_change_warning1'])
                return render(request,'changepassword.html',context)
        else:
            messages.warning(request,all_messages['password_change_warning2'])
            return render(request,'changepassword.html',context)
    return render(request,'changepassword.html')

@login_required
def addjob(request):
    if request.method == "POST":
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
        
        job = AddJobModel(
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
            created_by=current_user,
        )
        job.save()
        messages.success(request,all_messages['addjob_success'])
        return redirect('dashboard')
    return render(request,'recruiter/addjob.html')

@login_required
def viewalljob(request):
    current_user = request.user
    job = AddJobModel.objects.all()
    jobDict={
        'job':job
    }
    return render(request,'viewalljob.html',jobDict)

@login_required
def deletejob(request,jobid):
    job = AddJobModel.objects.get(id = jobid)
    job.delete()
    return redirect('dashboard')

@login_required
def editjob(request,jobid):
    job = AddJobModel.objects.get(id = jobid)
    jobDict={
        'job' : job
    }
    if request.method == "POST":
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

        job = AddJobModel(
            id = jobid,
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
            created_by=current_user,
        )
        job.save()
        messages.success(request,all_messages['editjob_success'])
        return redirect('dashboard')
    return render(request,'recruiter/editjob.html',jobDict)

@login_required
def viewsinglejob(request,jobid):
    job =AddJobModel.objects.get(id=jobid)
    jobDict={
        'job':job
    }
    return render(request,'viewsinglejob.html',jobDict)