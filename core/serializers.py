from rest_framework import serializers

from . import models


class SubmissionSerializer (serializers.ModelSerializer):
    class Meta:
        model = models.Submission
        fields = '__all__'


class CodeSerializer (serializers.ModelSerializer):
    password = serializers.CharField (write_only = True)
    
    class Meta:
        model = models.Code
        fields = '__all__'
