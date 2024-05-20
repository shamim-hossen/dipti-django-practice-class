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
2. Then in `urls.py` file add `path` of homePage. 
```bash
from django.contrib import admin
from django.urls import path
from myProject.views import homePage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homePage/', homePage, name='homePage'),
]
```
you can import all fuction to write * `from myProject.views import *` insted of homePage, <br>
Also, you can use empty sting to display webpage at the root url ` path('', homePage, name='homePage'), `

</details>

<details>
<summary>Day03-Render template & template language</summary>

## Static file add in django
> For template rendering or link html, css, js file to django project you need to add static file in django setting 
1. Create `static` and `templates` folder, where manage.py is located.
2. In `setting.py` file add STATICFILES_DIRS to tell where static folder will be located
```
STATICFILES_DIRS = [
    BASE_DIR / "static",
    "/var/www/static/",
]
```
3. Now add templates folder location in `manage.py` setting, where `'DIRS': [BASE_DIR, 'templates'],`
```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR, 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```
## Rendering Template
1. Create a custom function,where return django render function in `views.py` for render html file 
```
from django.shortcuts import render

def homePage(request):
    return render(request, 'homePage.html')
```
2. Create URL path for that custom homePage function
```
from django.contrib import admin
from django.urls import path
from myProject.views import homePage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homePage/', homePage, name='homePage'),
]
```
3. Now Create `homePage.html` template file under `templates folder`
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>index</title>
</head>
<body>
    <h1>Rendering template</h1>
</body>
</html>
```
>(html file name will be that custom homePage function argument, which is given `'homePage.html'`) 
<hr>

| Feature          | Description                                            | Example                                         |
|------------------|---------------------------------------------------------|-------------------------------------------------|
| Template Language | Special syntax for dynamic content within HTML templates  | `{{ user.username }}`                             |
| Template Literals | A way to define strings in Python code (not Django specific) | `f"Hello, {name}!"`                               |
| Template Mastering | A technique for creating base templates with reusable elements (headers, footers) and extending them with child templates for specific content.    | `base.html` (base template), <br>`home.html` (extends base.html) |
| Template Engine  | Processes templates, parses DTL, generates final HTML     | (Behind the scenes) Renders templates based on DTL |
<hr>

## Template language
1. For using template language, you need to pass contex or dictionary from `views.py`
```
from django.shortcuts import render

def homePage(request):
    myDictionary={
        'key': 'value',
        'name': 'Shamim',
        'roll': '101'
    }
    return render(request, 'homePage.html', myDictionary)
```
2. check url path add or not in `urls.py` file, for that fuction 
```
from django.contrib import admin
from django.urls import path
from myProject.views import homePage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homePage/', homePage, name='homePage'),
]
```
3. Now use template language in `homePage.html`
```
    <table id="customers">
        <tr>
          <th>Key</th>
          <th>Name</th>
          <th>Roll</th>
        </tr>
        <tr>
          <td>{{key}} </td>
          <td>{{name}}</td>
          <td>{{roll}} </td>
        </tr>
      </table>
```
</details>

<details>
<summary>Day04-Render </summary>
</details>
