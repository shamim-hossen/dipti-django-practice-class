<div align="center">
<h1>Dipti Django Practice Classes</h1>
</div>

<details>
<summary>Day01-Create python environment & Django project</summary>

## Windows terminal use
1. Open cmd with windows startup or goto project folder path and write `cmd` and hit enter or `shift` right click
2. Open project in vscode. For this: `code .`
3. Make cmd defalut in vscode. For this, goto vscode terminal select dropdown and make cmd in default terminal

## Create python virtual environment
1. Check python install or not?.if install then goto next step 
`python --version` or `py -V`
2. For creating py environment, give command: `python -m venv env`
3. Then activate env, for this goto `.\env\Scripts\activate` path,and hit enter
4. Go back from env folder with command: `cd ../..`
5. If you want to deactivate environment, Simply write `deactivate` in terminal and hit enter

## Create django project 
1. Check django install or not? To check,command: `pip freeze` or `pip list` If django not install that project.give command `pip install django`
2. For creating django project command: `django-admin startproject Project_Name`
2. Go to Project folder, command: `cd Project_Name` 
3. For run server, command: 
```bash 
python manage.py runserver
``` 
</details>


<details>
<summary>Day02-Django superuser & Database view</summary>   

## Django Database Migrations
1. Always perform makemigrations first to initialize the schema (For database table) `py manage.py makemigrations`
2. Then Applies any changes you've made to Django models `py manage.py migrate`
3. To create super user, command: `py manage.py createsuperuser` and give username, email, password

## Showing text in website with HttpResponse
1. Create `views.py` file in project
```bash
from django.shortcuts import HttpResponse

def homePage(request):
    return HttpResponse("Welcome to our website")
```
2. Then in `urls.py` file add `path` of homePage. you can import all fuction to write * (import *) insted of homePage
```bash
from django.contrib import admin
from django.urls import path
from myProject.views import homePage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homePage/', homePage, name='homePage'),
]
```

</details>