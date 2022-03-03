from rest_framework import serializers
from productivity.models import Productivity

class ProductivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Productivity
        fields = ('id', 'date', 'duration', 'author')