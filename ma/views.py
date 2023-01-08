from django.shortcuts import render
from django.http import HttpResponse
import rest_framework
import time
from . import models, serializers
from rest_framework.renderers import JSONRenderer
# Create your views here.
import io
from rest_framework.parsers import JSONParser



def index(request):
    if request.user.is_authenticated==True and request.user.has_perm('ma.ma')==True:
        #mydata=models.Result.objects.all()[1:10]
        mydata=models.Result.objects.filter(examination_id=5031)[1:1000]
        serializer = serializers.ResultSerializer(mydata, many=True, context={'request': request})
        content = JSONRenderer().render(serializer.data)
        stream = io.BytesIO(content)
        fdata = JSONParser().parse(stream)
        help='This is MA'
        return render(request, "ma/index.html", {"help":help,"appname":"Clinical Laboratory", 'data':fdata,'current_datetime':(time.strftime("%Y-%m-%d %H:%M:%S ") + time.tzname[0])})
    else:
        html = "<html><body><a href=authentication/login>Login</a></html>"
        return HttpResponse(html)
        


from . import models, serializers
from rest_framework import viewsets
from rest_framework import permissions



#class ResultViewSet(viewsets.ModelViewSet):
class ResultViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.Result.objects.all().order_by('sample_id')
    serializer_class = serializers.ResultSerializer
    permission_classes = [permissions.IsAuthenticated]


class EditResultViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.Result.objects.all().order_by('sample_id')
    serializer_class = serializers.EditResultSerializer
    permission_classes = [permissions.IsAuthenticated]
    

class ExaminationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.Examination.objects.all()
    serializer_class = serializers.ExaminationSerializer
    permission_classes = [permissions.IsAuthenticated]
