# django-install
django installation and first minimal project as production server with apache2
Although a lot many online tutorials are avaialble for django installation and starting first project, they all rely on its internal server.\
This help is step-by-step guide for making this bare-bone project working with apache2\
I saw many online resources, but, comprehansive help for newbee is missing\
#Installation
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
  * -rw-r--r-- 1 root root 171 Nov 29 11:31  for Files
  * drwxr-xr-x 4 root root 4096 Nov 29 11:22 for Folders

#### login.html

```
  <form method=post>
    {% csrf_token %}
  {{form}}
  <input type=submit name=submit value=login>
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
  
