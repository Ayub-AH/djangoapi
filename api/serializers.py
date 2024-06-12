from rest_framework import serializers
from .models import Hadith

class HadithSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hadith
        fields = "__all__"
