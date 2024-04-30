from django.shortcuts import redirect, render
from myApp.models import CustomUserModel, RecipeModel
from django.contrib.auth import authenticate, login, logout

def signup(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        gender=request.POST.get('gender')
        age=request.POST.get('age')
        city=request.POST.get('city')
        country=request.POST.get('country')
        user_type=request.POST.get('user_type')

        if password==confirm_password:
            user=CustomUserModel.objects.create_user(
                username=username,
                password=confirm_password,
                email=email,
                Gender=gender,
                Age=age,
                City=city,
                Country=country,
                UserType=user_type,
            )
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

def dashboard(request):
    return render(request, 'dashboard.html')

def logoutfn(request):
    logout(request)
    return redirect('signin')


def profile(request):
    return render(request, 'profile.html')

def viewrecipe(request):
    if request.user.UserType=='chef':
        recipe=RecipeModel.objects.filter(OwnerOfPost=request.user)
    else:
        recipe=RecipeModel.objects.all()
    contex={
        'recipe':recipe,
    }
    return render(request, 'viewrecipe.html',contex)

def addrecipe(request):
    if request.user.UserType=='chef':
        if request.method=='POST':
            title=request.POST.get('title')
            image=request.POST.get('image')
            description=request.POST.get('description')
            prep_time=request.POST.get('prep_time')
            cook_time=request.POST.get('cook_time')
            servings=request.POST.get('servings')
            OwnerOfPost=request.user

            recipe=RecipeModel(
                Title=title,
                RecipeImage=image,
                Description=description,
                PrepTime=prep_time,
                CookTime=cook_time,
                Servings=servings,
                OwnerOfPost=OwnerOfPost,
            )
            recipe.save()
            return redirect('viewrecipe')
        return render(request, 'addrecipe.html')
    else:
        logout(request)
        return redirect('signin')