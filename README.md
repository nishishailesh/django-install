# django-install
django installation and first minimal project as production server with apache2\
Although a lot many online tutorials are avaialble for django installation and starting first project, they all rely on its internal server.\
This help is step-by-step guide for making this bare-bone project working with apache2\
I saw many online resources, but, comprehansive help for newbee is missing\
# Installation
  1. debian 11.* login as root / use su / use sudo
  2. basic knowledge of mysql,apache2 and python required
  3. ``apt install python3-django``
  4. you need to do two things: start project -> startapp to complate bare minimum application
 # startproject
  5. I will install my project in /usr/share/nchs folder (/usr/share have default permission for web access in debian)
  6. ``mkdir /usr/share/nchs``
  7. `` cd /usr/share/nchs``
  8. ``django-admin startproject dj`` (see a folder created in /usr/share/nchs/dj , with one more dj named folder inside and manage.py)
  9. ``cd /usr/share/nchs/dj`` (to run "python namage.py ..." commands)
  10. edit /usr/share/nchs/dj/dj/settings.py
  11. some chnages required as shown below
  
```
DEBUG = True  #Not edited to view errors during this experiment

#For using mysql database (remove sqlite details)
#change name of database, user,password as per your installation
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'resident',
        'USER' : 'main_user',
        'PASSWORD' : 'main_pass',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

#a lot of time was wasted because STATIC_URL in original file was '/static/'
STATIC_URL = '/dj/static/'

#to get proper css and js configuration static root needs to be defined. 
#leter on 'collectstatic' command will be used to get admin static files in this folder
STATIC_ROOT="/usr/share/nchs/dj/static"

```

  10. ``python3 manage.py  migrate``  (see various tables created in resident database)
  11. ``python3 manage.py  createsuperuser`` (this will be useful to test weather admin module is properly working)
  12. give admin email,password when asked
  13. ``python3 manage.py  collectstatic`` (this will copy files in STATIC_ROOT folder , in our case, admin files from django installation)
  14. Edit wsgi.py file in /usr/share/nchs/dj/dj folder
  15. comment a line to ensure that mutiple projects work under apache2

    #os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dj.settings')
    os.environ["DJANGO_SETTINGS_MODULE"] = "dj.settings"

  16. create/edit /etc/apache2/conf-enabled/common.conf (This is to ensure that other projects hosted under apache2 remain as it is).  python-path is : saperated paths where project is installed. so only one dj, not two dj is in the path. Alias is necessary because browser will ask this location to get static files. see the absolute path of project static files is required. In fact, it is ``Alias STATIC_URL STATIC_ROOT``

```
    WSGIDaemonProcess Pone processes=3 threads=15 python-path=/usr/share/nchs/dj
    WSGIScriptAlias /dj /usr/share/nchs/dj/dj/wsgi.py   
    <Directory /usr/share/nchs/dj/dj>
        WSGIProcessGroup Pone
        Require all granted
    </Directory>
Alias /dj/static /usr/share/nchs/dj/static

```

  17. service apache2 restart
  18. go to: http://127.0.0.1/dj/admin
  19. For most use case this app (admin) is not useful. For routine login system we need saperate app.

# startapp
* in this example two apps will be created
  - authentication (this will you auth app built in to django basic installation)
  - home
* if your project directory is dj ( in which manage.py is located) , run following command
* ``python3 manage.py startapp authetication``
* ``python3 manage.py startapp home``
* See that, main dj folder have three subfolders ( dj,authentication, home )
* It was very nice to learn that basic login/logout/change password system can be implimented by creating few templates and few line of code
## authentication app
* It is based on django.contrib.auth (its entry already there in settings.py)
### settings.py (in main project folder dj)
* This file already exist in main project folder (dj/dj)
* in INSTALLED_APPS list add two more members, authentication and home. This will make project to search for them in project base folder
```
    INSTALLED_APPS = [
    #'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'authentication',
    'home'
    ]
```
* add following directive in settings.py
* ```LOGIN_REDIRECT_URL='/dj/'```
* This is requirement of auth app. It will redirect to this URL if login is successful. So, login form have no need for usual <form action=xyz>
  
### urls.py (in main project folder dj)
* make following changes
  
```
from django.urls import path, include
import home.views
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('authentication/', include("django.contrib.auth.urls")),      #this is a string. not required to import
    path('', home.views.index, name='home')
    
]
```
* In home app folder there is views.py. It will have index() function (to be writtern later on)
* This index() will be called when path is empty (just 127.0.0.0.1/dj)
* 127.0.0.0.1/dj/authentication/XYZ will be various urls imported from auth app

  ### changes in authentication folder
  * create authentication/templates/registration folder from commandline. 
  * in it create login.html,loggged_out.html, password_change_form.html,password_change_done.html by linux ```touch``` command
  * Commandline creation will set proper permissions. 
  * If root is owner of this file and folders following is required
  * -rw-r--r-- 1 root root 171 Nov 29 11:31  ----> for Files
  * drwxr-xr-x 4 root root 4096 Nov 29 11:22 ----> for Folders

#### login.html

```
  <form method=post>
    {% csrf_token %}
  {{form}}
  <input type=submit name=submit value=login>curl -H 'Accept: application/json; indent=4' -u root:DNArna@123 http://127.0.0.1/dj/ma
  </form>
```

#### loggged_out.html
  ```
  <a href="{%url 'login' %}">Login</a>
  ```

  
#### password_change_form.html
```
<form method=post>
    {% csrf_token %}
{{form}}
<input type=submit name=submit value='change password'>
</form>
  
```  
#### password_change_done.html
```
<h3>Password Changed. Login using new password</h3>
<a href="{%url 'login' %}">Login</a> 
```  
* interestingly, you need only templates to be created. auth app will look for them and use it as required.
* {% csrf_token %} is used in all forms for security reason
* {{form}} is a variable data passed by auth views to this template.
* Unlike html form there is no need for action. This is required, because action is not determined by auth, but by settings.py LOGIN_REDIRECT_URL declaration
* password_change_form ultimately randers password_change_done if change is successful. Again no action to be specified in form
* These 4 files are just enough to start app working.
* Now, some chnages in home app is required

## home app
* Two files are needed. views.py already exist. Templates/index.html needs to be created. Ensure permissions as above  
#### views.py

```
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect   ##### because it is used if user is not authenticated
# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return render(request, "index.html", {})
    else:
        return redirect('login')
        #return redirect('authentication/login')
```
* request object is passed by django engine to this function.
* one of the element of request object is user
* So, actually, admin app takes user/password, verify their correctness and update request object.
* redirect() uses url name. It is interesting. because, if you know name , the full path (commented line just below it) is avoided.
* use of name, instead of full path is good, because, it avoids actual name of auth app (app-name could be account/authentication/login etc)  
#### index.html
* this name, index was used in urls.py in main app folder. 
* Flow of information is -> login.html -> admin processing -> LOGIN_REDIRECT_URL -> "" is matching home.views.home() -> ( index.html is randered or redirected to "login" name definded by auth
```
<html>
    <body>
        It is Home
        <a href="{% url 'logout' %}">Logout</a>
        <a href="{% url 'password_change' %}">Change Password</a>
    </body>
</html>
```
* logged in users are given chance to change password.
* notice use of 'logout' name in inverted comma. This ensure that the template do not have to write real name of external app.
# Finally  
* restart apache2 ```service apache2 restart```  
* http://127.0.0.1/dj
* delete/edit code in any way and see error messages on screen. Without it, following this tutorial as copy-paste activity will not help

# django RESTful API
soon, I realised that, using REST API with django is second most important thing to learn (after setting authentication system)\
```apt install django-resfulapi```\
the new app using REST API is called "ma"\
```python3 manage.py startapp ma```
  
#### settings.py (in main project folder)
```
INSTALLED_APPS = [
    'rest_framework'
]
```
  
#### urls.py (in main project folder)
```
import home.views, ma.views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'result', ma.views.ResultViewSet)

urlpatterns = [
    path('ma/', include(router.urls)),
    #following is commented because I was getting template not found error
    #path('ma/api-result/', include('rest_framework.urls', namespace='rest_framework'))

]
```
#### models.py in ma app folder (I am creating table called "result" with classname "Result". )
```
from django.db import models

# Create your models here.

class Result(models.Model):
    sample_id = models.BigIntegerField(primary_key=True)
    examination_id = models.IntegerField()
    result = models.CharField(max_length=5000, blank=True, null=True)
    recording_time = models.DateTimeField(blank=True, null=True)
    recorded_by = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'result'
        unique_together = (('sample_id', 'examination_id'),)
  ```
  the table will be created manually in mysql.\
  If one wants to create it by django 
  1. set  ```managed=True```
  2. run ```makemigrations``` and ```migrate``` django commands
  3. if ```managed=True``` is done after creating tables manually once, delete repective entry from mysql table for migrations. Otherwise it will never use managed=True settings
  
####  serializers.py in ma app folder
```
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Result

class ResultSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Result
        fields = ['url', 'sample_id', 'examination_id', 'result']
```
  
#### views.py in ma app folder
```
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


import ma.models, ma.serializers
from rest_framework import viewsets
from rest_framework import permissions



class ResultViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ma.models.Result.objects.all().order_by('sample_id')
    serializer_class = ma.serializers.ResultSerializer
    permission_classes = [permissions.IsAuthenticated]
```
  
run ```collectstatic``` command\
restart apache2\
login\
```127.0.0.1/dj/ma```\
edit /etc/apache2-conf/conf-enabled/common.conf as described above\
add    line ```WSGIPassAuthorization On``` outside any section, to make curl work\
restart apache2\
<<<<<<< HEAD
```curl -H 'Accept: application/json; indent=4'  -u UUUU:PPPP http://127.0.0.1/dj/ma/```
see / folloing ma.\
=======
```curl -H 'Accept: application/json; indent=4'  -u user:password http://127.0.0.1/dj/ma/```
  *use "API command" (inverted comma) if command contain @ in password field

```curl -H 'Accept: application/json; indent=4'  -u user http://127.0.0.1/dj/ma/```
  * password will be asked on prompt

see / following ma.\
I spent 30 minutes figuring out this mistake\
play, experiment
  
 # settings.py Cookie expiration
```
SESSION_COOKIE_AGE=300   #expire in 300 seconds
SESSION_EXPIRE_AT_BROWSER_CLOSE=True #expire when browser close
```
