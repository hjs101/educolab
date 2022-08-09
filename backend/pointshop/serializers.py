from rest_framework import serializers
from .models import PTitle

class TitleMainSerializer(serializers.ModelSerializer):

    class Meta:
        model = PTitle
        fields = '__all__'

class TitleSerializer(serializers.ModelSerializer):

    class Meta:
        model = PTitle
        fields = ('id','title',)