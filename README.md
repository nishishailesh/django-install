# django-install
django installation and first minimal project as production server with apache2
Although a lot many online tutorials are avaialble for django installation and starting first project, they all rely on its internal server.\
This help is step-by-step guide for making this bare-bone project working with apache2\
I saw many online resources, but, comprehansive help for newbee is missing\
#Installation
  1. debian 11.* login as root / use su / use sudo
  2. basic knowledge of mysql,apache2 and python required
  3. ``apt install python3-django``
  4. I will install my project in /usr/share/nchs folder (/usr/share have default permission for web access in debian)
  5. ``mkdir /usr/share/nchs``
  6. `` cd /usr/share/nchs``
  7. ``django-admin startproject dj`` (see a folder created in /usr/share/nchs/dj , with one more dj named folder inside and manage.py)
  8. ``cd /usr/share/nchs/dj`` (to run "python namage.py ..." commands)
  9. edit /usr/share/nchs/dj/dj/settings.py
  10. some chnages required as shown below
  
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
<VirtualHost *:80>
    WSGIDaemonProcess Pone processes=3 threads=15 python-path=/usr/share/nchs/dj
    WSGIScriptAlias /dj /usr/share/nchs/dj/dj/wsgi.py   
    <Directory /usr/share/nchs/dj/dj>
        WSGIProcessGroup Pone
        Require all granted
    </Directory>
</VirtualHost>
Alias /dj/static /usr/share/nchs/dj/static

```

  17. service apache2 restart
  18. go to: http://127.0.0.1/dj/admin

