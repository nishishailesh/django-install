from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return render(request, "index.html", {})
        #html = "<html><body>It is Home</body></html>"
        #return HttpResponse(html)
    else:
        return redirect('login')
        #return redirect('authentication/login') #Ths works but another app name is required
        #html = "<html><body>Not logged in</body></html>"
        #return HttpResponse(html)
