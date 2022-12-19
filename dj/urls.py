"""dj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django.contrib import admin
from django.urls import path, include
import home.views, ma.views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'result', ma.views.ResultViewSet)
router.register(r'rresult', ma.views.MyResultViewSet)

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('authentication/', include("django.contrib.auth.urls")),      #this is a string. not required to import
    path('', home.views.index, name='home')  ,  
    
    #path('ma', ma.views.index, name='ma'),    
    path('ma/', include(router.urls)),
    #path('ma/api-result/', include('rest_framework.urls', namespace='rest_framework'))
    path('ma/my/', include('ma.urls')),

]

'''
    authentication/ login/ [name='login']
    authentication/ logout/ [name='logout']
    authentication/ password_change/ [name='password_change']
    authentication/ password_change/done/ [name='password_change_done']
    authentication/ password_reset/ [name='password_reset']
    authentication/ password_reset/done/ [name='password_reset_done']
    authentication/ reset/<uidb64>/<token>/ [name='password_reset_confirm']
    authentication/ reset/done/ [name='password_reset_complete']
    [name='home']
'''
