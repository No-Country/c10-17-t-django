from rest_framework import serializers
from aplications.authentication.models import FollowUp

class FollowUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = FollowUp
        fields = '__all__'