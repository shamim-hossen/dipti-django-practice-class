from django.shortcuts import redirect, render
from myApp.models import CustomUserModel
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        username=request.POST.get('username')
        profile_picture=request.FILES.get('profile_picture')
        date_of_birth=request.POST.get('date_of_birth')
        blood_group=request.POST.get('blood_group')
        address=request.POST.get('address')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        usertype=request.POST.get('usertype')

        if password==confirm_password:
            user=CustomUserModel.objects.create_user(
                username=username,
                password=password,
            )
            user.first_name=fname
            user.last_name=lname
            user.email=email
            user.ProfilePicture=profile_picture
            user.DateOfBirth=date_of_birth
            user.BloodGroup=blood_group
            user.Address=address
            user.UserType=usertype
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