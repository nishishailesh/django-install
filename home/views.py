from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
import time
import ma.models, ma.serializers
from rest_framework.renderers import JSONRenderer

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return render(request, "home/index.html",{"urls":"urls.urlpatterns"})
        
    else:
        return redirect('login')


