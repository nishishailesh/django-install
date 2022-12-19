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


class MyResultViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ma.models.Result.objects.all().order_by('sample_id')
    serializer_class = ma.serializers.MyResultSerializer
    permission_classes = [permissions.IsAuthenticated]

# following is manual View  (done by above class without much coding)

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt #required for easy curl testing
from rest_framework.parsers import JSONParser

@csrf_exempt
def result_select(request):
    if request.method == 'GET':             #view all data
        result = ma.models.Result.objects.all()
        serializer = ma.serializers.MyResultSerializer(result, many=True)
        return JsonResponse(serializer.data, safe=False)
        
        
@csrf_exempt
def result_insert(request):
    if request.method == 'POST':                #save new
        data = JSONParser().parse(request)
        serializer = ma.serializers.MyResultSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def result_update_delete(request, pk):
    try:
        result = ma.models.Result.objects.get(pk=pk)
    except ma.models.Result.DoesNotExist:
        return HttpResponse("status=404")

    if request.method == 'GET':                 #Get form for edit
        serializer = ma.serializers.MyResultSerializer(result)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':               #update
        data = JSONParser().parse(request)
        serializer = ma.serializers.MyResultSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':            #delete
        result.delete()
        return HttpResponse(status=204)
        
