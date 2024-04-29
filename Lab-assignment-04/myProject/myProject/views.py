from django.shortcuts import redirect, render
from myApp.models import CustomUserModel, RecipeModel
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required

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
        usertype=request.POST.get('usertype')

        if password==confirm_password:
            user=CustomUserModel.objects.create_user(
                username=username,
                password=password,
            )
            user.email=email
            user.Gender=gender
            user.Age=age
            user.City=city
            user.Country=country
            user.UserType=usertype
            user.save()
            return redirect('signin')
        else:
            return redirect('signup')
    return render(request, 'signup.html')

def signin(request):
    if request.method=="POST":
        uname=request.POST.get('uname')
        password=request.POST.get('password')
        
        user = authenticate(
            username=uname,
            password=password,
        )
        print(f'Logged in user: {user}')
        print(f'Logged in username: {uname}')
        if user:
            login(request,user)
            return redirect('dashboard')
        else:
            return redirect('signin')
    return render(request, 'signin.html')


@login_required
def dashboard(request):
    recipe=RecipeModel.objects.all()
    contex={
        'recipe':recipe,
    }
    return render(request, 'dashboard.html',contex)

@login_required
def logoutpage(request):
    logout(request)
    return redirect('signin')

@login_required
def profile(request):
    profile=CustomUserModel.objects.filter(username=request.user)
    contex={
        'profile':profile,
    }
    return render(request,'profile.html',contex)




@login_required
def addrecipe(request):
    if request.user.UserType == 'chef':
        if request.method=='POST':
            RecipeTitle=request.POST.get('RecipeTitle')
            Ingredients=request.POST.get('Ingredients')
            Instructing=request.POST.get('Instructing')
            PreparationTime=request.POST.get('PreparationTime')
            CookingTime=request.POST.get('CookingTime')
            TotalTime=request.POST.get('TotalTime')
            DifficultyLevel=request.POST.get('DifficultyLevel')
            NutritionalInformation=request.POST.get('NutritionalInformation')
            SampleRecepeImage=request.FILES.get('SampleRecepeImage')
            RecipeCategory=request.POST.get('RecipeCategory')
            Tags=request.POST.get('Tags')
            TotalCalories=request.POST.get('TotalCalories')
            loginUsername=request.user

            recipe=RecipeModel(
                RecipeTitle=RecipeTitle,
                Ingredients=Ingredients,
                Instructing=Instructing,
                PreparationTime=PreparationTime,
                CookingTime=CookingTime,
                TotalTime=TotalTime,
                DifficultyLevel=DifficultyLevel,
                NutrationalInformation=NutritionalInformation,
                SampleRecepeImage=SampleRecepeImage,
                RecipeCategory=RecipeCategory,
                Tags=Tags,
                TotalCalories=TotalCalories,
                OwnerOfJobPost=loginUsername,
            )
            recipe.save()
            return redirect('viewrecipe')
        return render(request,'addrecipe.html')
    else:
        logout(request)
        return redirect('signin')
    
@login_required
def viewrecipe(request):
    if request.user.UserType== 'chef':
        recipe=RecipeModel.objects.filter(OwnerOfJobPost = request.user)
    else:
        recipe=RecipeModel.objects.all()

    contex={
        'recipe':recipe,
    }
    return render(request,'viewrecipe.html',contex)

@login_required
def deleterecipe(request,myid):
    recipe=RecipeModel.objects.get(id=myid)
    recipe.delete()
    return redirect('viewrecipe')

@login_required
def editrecipe(request,myid):
    recipe=RecipeModel.objects.get(id=myid)
    contex={
        'recipe':recipe,
    }
    return render(request, 'editrecipe.html',contex)

@login_required
def updaterecipe(request):
    if request.method=='POST':
        myid=request.POST.get('myid')
        RecipeTitle=request.POST.get('RecipeTitle')
        Ingredients=request.POST.get('Ingredients')
        Instructing=request.POST.get('Instructing')
        PreparationTime=request.POST.get('PreparationTime')
        CookingTime=request.POST.get('CookingTime')
        TotalTime=request.POST.get('TotalTime')
        DifficultyLevel=request.POST.get('DifficultyLevel')
        NutritionalInformation=request.POST.get('NutritionalInformation')
        SampleRecepeImage=request.FILES.get('SampleRecepeImage')
        RecipeCategory=request.POST.get('RecipeCategory')
        Tags=request.POST.get('Tags')
        TotalCalories=request.POST.get('TotalCalories')
        loginUsername=request.user

        if SampleRecepeImage:
            recipe=RecipeModel(
                id=myid,
                RecipeTitle=RecipeTitle,
                Ingredients=Ingredients,
                Instructing=Instructing,
                PreparationTime=PreparationTime,
                CookingTime=CookingTime,
                TotalTime=TotalTime,
                DifficultyLevel=DifficultyLevel,
                NutrationalInformation=NutritionalInformation,
                SampleRecepeImage=SampleRecepeImage,
                RecipeCategory=RecipeCategory,
                Tags=Tags,
                TotalCalories=TotalCalories,
                OwnerOfJobPost=loginUsername,
            )
        else:
            recepeid=RecipeModel.objects.get(id=myid)
            recipe=RecipeModel(
                id=myid,
                RecipeTitle=RecipeTitle,
                Ingredients=Ingredients,
                Instructing=Instructing,
                PreparationTime=PreparationTime,
                CookingTime=CookingTime,
                TotalTime=TotalTime,
                DifficultyLevel=DifficultyLevel,
                NutrationalInformation=NutritionalInformation,
                SampleRecepeImage=recepeid.SampleRecepeImage,
                RecipeCategory=RecipeCategory,
                Tags=Tags,
                TotalCalories=TotalCalories,
                OwnerOfJobPost=loginUsername,
            )
        
        recipe.save()
        return redirect('viewrecipe')

@login_required
def viewfull(request,myid):
    recipe=RecipeModel.objects.filter(id=myid)
    contex={
        'recipe':recipe,
    }
    return render(request,'viewfull.html',contex)

