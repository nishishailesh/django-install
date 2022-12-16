from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Result

class ResultSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Result
        fields = ['url', 'sample_id', 'examination_id', 'result']
