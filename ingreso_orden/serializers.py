from .models import OrdenRetiro
from rest_framework import serializers
from django.utils import timezone

class OrdenRetiroSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdenRetiro
        fields = "__all__"