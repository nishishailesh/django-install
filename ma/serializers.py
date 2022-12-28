from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Result
from ma.models import Examination

class ResultSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Result
        fields = ['id','sample_id', 'examination_id', 'result','recording_time','recorded_by']


class ExaminationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Examination
        fields = ['id', 'name', 'sample_requirement', 'edit_specification', 'description' ]
