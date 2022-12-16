from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.

def index(request):
    if request.user.is_authenticated:
        html = "<html><body>Moving Average</body></html>"
        return HttpResponse(html)
    else:
        html = "<html><body><a href=authentication/login>Login</a></html>"
        return HttpResponse(html)
        


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
