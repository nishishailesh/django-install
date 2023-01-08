from django.shortcuts import render
from django.http import HttpResponse
import rest_framework
import time
from . import models, serializers
from rest_framework.renderers import JSONRenderer
from django.shortcuts import redirect
from django.contrib.auth.decorators import user_passes_test

# Create your views here.

def index(request):
    if request.user.is_authenticated==True and request.user.is_staff==True:
        mydata=models.Intake.objects.all()[1:10].using('food')
        serializer = serializers.IntakeSerializer(mydata, many=True, context={'request': request})
        content = JSONRenderer().render(serializer.data)
        help='This is FOOD'
        return render(request, "food/index.html", {"help":help,"appname":"Food", 'data':content,'current_datetime':(time.strftime("%Y-%m-%d %H:%M:%S ") + time.tzname[0])})
    else:
        return redirect('login')
        #return HttpResponse(html)
        


from . import models, serializers
from rest_framework import viewsets
from rest_framework import permissions



class IntakeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.Intake.objects.all().using('food')
    serializer_class = serializers.IntakeSerializer
    permission_classes = [permissions.IsAuthenticated]


class MyfoodViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.Myfood.objects.all().using('food')
    serializer_class = serializers.MyfoodSerializer
    #permission_classes = [permissions.IsAuthenticated]     #for authentication
