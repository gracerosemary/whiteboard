from rest_framework import serializers
from .models import Whiteboard

class WhiteboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Whiteboard
        fields = ['student', 'created_at', 'structure', 'action', 'method']