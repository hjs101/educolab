from rest_framework import serializers

from accounts.serializers import SchoolInfoSerializer
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    school = SchoolInfoSerializer(read_only=True)

    class Meta:
        model = Event
        fields = '__all__'