from django.shortcuts import render,redirect,get_object_or_404
from todoApp.models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from datetime import date

all_messages={
    'signup_success':'Signup successful!',
    'signin_success':'Signin successful!',
}

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, all_messages['signup_success'])
            return redirect('signin')
    else:
        form = CustomUserCreationForm()

    return render(request, 'common/signup.html', {'form': form})
            

def signin(request):
    if request.method=="POST":
        form=CustomUserAuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            messages.success(request,all_messages['signin_success'])
            return redirect('dashboard')
    else:
        form=CustomUserAuthenticationForm()
    return render(request,'common/signin.html',{'form':form})

@login_required
def dashboard(request):
    # u_task=TaskModel.objects.filter(task_status='on_going')
    u_task=TaskModel.objects.filter(due_date__gt=date.today())
    u_count=TaskModel.objects.filter(task_status='on_going').count()
    c_task=TaskModel.objects.filter(task_status='completed')
    c_count=TaskModel.objects.filter(task_status='completed').count()
    print(u_count,c_count)
    return render(request,'common/dashboard.html',{'task':u_task, 'count':u_count,'c_task':c_task,'c_count':c_count})

@login_required
def logoutpage(request):
    logout(request)
    return redirect('signin')

@login_required
def addcategory(request):
    if request.method=="POST":
        current_user=request.user
        form=CustomCategoryForm(request.POST)
        if form.is_valid():
            category=form.save(commit=False)
            category.user=current_user
            category.save()
            return redirect('categorylist')
    else:
        form=CustomCategoryForm()
    return render(request,'user/addcategory.html',{'form':form})

@login_required
def categorylist(request):
    cat=CategoryModel.objects.all()
    return render(request,'user/categorylist.html',{'cat':cat})

@login_required
def categorydel(request,catid):
    cat=get_object_or_404(CategoryModel,id=catid)
    cat.delete()
    return redirect('categorylist')


@login_required
def editcategory(request,catid):
    cat=get_object_or_404(CategoryModel,id=catid)
    if request.method=="POST":
        form=CustomCategoryForm(request.POST,instance=cat)
        if form.is_valid():
            form.save()
            return redirect('categorylist')
    else:
        form=CustomCategoryForm(instance=cat)
    return render(request,'user/editcategory.html',{'form':form,'cat':cat})

@login_required
def addtask(request):
    if request.method == "POST":
        form=CustomTaskForm(request.POST)
        if form.is_valid():
            # form=form.save(commit=False)
            # form.category=
            form.save()
            return redirect('tasklist')
    else:
        form=CustomTaskForm()
    return render(request,'user/addtask.html',{'form':form})

@login_required
def tasklist(request):
    task=TaskModel.objects.all()
    print(task)
    return render(request,'user/tasklist.html',{'task':task})

@login_required
def taskdel(request,taskid):
    task=get_object_or_404(TaskModel,id=taskid)
    task.delete()
    return redirect('tasklist')

@login_required
def edittask(request,taskid):
    task=get_object_or_404(TaskModel,id=taskid)
    if request.method=="POST":
        form=CustomTaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasklist')
    else:
        form=CustomTaskForm(instance=task)
    return render(request,'user/edittask.html',{'form':form,'task':task})


def markascomp(request, taskid):
    task=get_object_or_404(TaskModel,id=taskid)
    task.task_status='completed'
    task.save()
    return redirect('dashboard')