from api.models import Mobile

from rest_framework import serializers


class MobileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Mobile
        fields="__all__"
        