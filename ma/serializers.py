from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Result


class ResultSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Result
        fields = ['url', 'id','sample_id', 'examination_id', 'result']

#manual work instead of ModelSerializer class

class MyResultSerializer(serializers.Serializer):
    sample_id = serializers.IntegerField()
    examination_id = serializers.IntegerField()
    result = serializers.CharField(max_length=5000, allow_blank=True)

    def create(self, validated_data):
        return Result.objects.create(**validated_data) # using models

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.sample_id = validated_data.get('sample_id', instance.sample_id)
        instance.examination_id = validated_data.get('examination_id', instance.examination_id)
        instance.result = validated_data.get('result', instance.result)
        instance.save()
        return instance

