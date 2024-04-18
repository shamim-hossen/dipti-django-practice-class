# create python virtual environment
 
1. check py install or not? if install then goto next step 
2. for creating py environment, give command: python -m venv env
3. then activate env, for this goto .\env\Scripts\activate path,and hit enter
4. go back from env folder with command: cd ../..

# create django project 
1. check django install or not? to check,command: pip freeze or pip list 
2. for creating django project command: django-admin startproject myProject
2. go to myProject folder, command: cd myProject 
3. run server, command: python manage.py runserver 