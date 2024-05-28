from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from schoolApp.models import CustomUserModel

def signuppage(request):
    if request.method=="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        if password==cpassword:
            user = CustomUserModel.objects.create_user(
                username=username,
                email=email,
                password=password,
                user_type="1",
            )
            user.save()
            return redirect('signinpage')
    return render(request,'common/signuppage.html')

def signinpage(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user=authenticate(
            username=username,
            password=password
            )
        if user:
            login(request,user)
            if request.user.user_type=="1":
                return redirect('adminpage')
            elif request.user.user_type=="2":
                return redirect('teacherdashboard')
            elif request.user.user_type=="3":
                return redirect('studentdashboard')
    return render(request,'common/signinpage.html')

@login_required
def profile(request):
    return render(request,'common/profile.html')

@login_required
def logoutpage(request):
    logout(request)
    return redirect('signinpage')

@login_required
def adminpage(request):
    return render(request,'myadmin/adminpage.html')






























