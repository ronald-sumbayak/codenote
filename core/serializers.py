import re

from django.core.validators import RegexValidator
from rest_framework import serializers

from .models import Code, Language, Reserved, Submission
from .views import LazyAPIView


class AlphaNumericField (serializers.CharField):
    default_error_messages = {
        'invalid':
            'AlphaNumeric characters only.'
    }
    
    def __init__ (self, **kwargs):
        super ().__init__ (**kwargs)
        self.validators.append (
            RegexValidator (
                re.compile (r'^[a-zA-Z0-9]+$'),
                message = self.error_messages['invalid']))


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
    uri = AlphaNumericField ()
    
    def validate_uri (self, value):
        try:
            self.set_validation_result (Code.objects.get (uri=value))
            return value
        except Code.DoesNotExist:
            try:
                Reserved.objects.get (word=value)
                raise LazyAPIView.Error (
                    ('uri', 'Sorry, this URL has been reserved for internal use (:'), 403)
            except Reserved.DoesNotExist:
                raise LazyAPIView.Error (('uri', 'Does not exists'), 404)


class SubmissionSerializer (serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = '__all__'


class CodeSerializer (serializers.ModelSerializer):
    password = serializers.CharField (write_only=True)
    
    class Meta:
        model = Code
        fields = '__all__'


class LanguageSerializer (serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'


