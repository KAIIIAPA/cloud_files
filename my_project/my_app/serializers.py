from rest_framework import serializers
from .models import Allfiles


class AllfilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Allfiles
        fields = ('file', 'created_at', 'creator')
