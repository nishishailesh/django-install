from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Intake
from .models import Myfood

class IntakeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Intake
        fields = ['id','food_id']


class MyfoodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Myfood
        fields = ['id', 'food_item' ]
