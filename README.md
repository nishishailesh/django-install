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
  8. edit /usr/share/nchs/dj/dj/settings.py
  9. some chnages required as shown below
  
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
'''
  10. ``python3 manage.py  migrate``
  
python3 manage.py  createsuperuser
service apache2 restart
service apache2 restart
service apache2 restart
service apache2 restart
service apache2 restart
service apache2 restart
service apache2 restart
service apache2 status
service apache2 status
service apache2 restart
service apache2 restart
service apache2 restart
service apache2 restart
service apache2 status
service apache2 status
service apache2 restart
ls /usr/lib/python3/dist-packages/django/contrib/admin/static
ls /usr/lib/python3/dist-packages/django/contrib/admin/static/admin/
python3 manage.py
python3 manage.py  collectstatic
ls
ls static/
service apache2 restart
service apache2 restart
pico /root/.bash_history
exit
tail -f /var/log/apache2/error.log
exit

