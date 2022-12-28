from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return render(request, "index.html", {"appname":"MA"})
    else:
        return redirect('login')
