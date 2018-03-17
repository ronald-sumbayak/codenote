from rest_framework import serializers

from core.models import Code
from core.views import LazyAPIView
from . import models


class ViewSerializer (serializers.Serializer):
    __validation_result = None
    
    def update (self, instance, validated_data):
        pass
    
    def create (self, validated_data):
        pass
    
    def set_validation_result (self, validation_result):
        self.__validation_result = validation_result
    
    @property
    def validation_result (self):
        return self.__validation_result


class URISerializer (ViewSerializer):
    uri = serializers.SlugField ()
    
    def validate (self, attrs):
        try:
            self.set_validation_result (Code.objects.get (uri = attrs.get ('uri')))
            return attrs
        except Code.DoesNotExist:
            raise LazyAPIView.Error ('Code Does Not Exists')


class SubmissionSerializer (serializers.ModelSerializer):
    class Meta:
        model = models.Submission
        fields = '__all__'


class CodeSerializer (serializers.ModelSerializer):
    password = serializers.CharField (write_only = True)
    
    class Meta:
        model = models.Code
        fields = '__all__'


class CompilerSerializer (serializers.ModelSerializer):
    class Meta:
        model = models.Compiler
        fields = '__all__'
