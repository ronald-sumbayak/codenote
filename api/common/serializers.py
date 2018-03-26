import rest_framework.serializers as rfserializer
from django.core.files.uploadedfile import InMemoryUploadedFile

from core import serializers
from core.models import Code, Language, Reserved
from core.serializers import AlphaNumericField, URISerializer, ViewSerializer
from core.views import LazyAPIView


class RefreshSerializer (serializers.ViewSerializer):
    password = rfserializer.CharField ()
    
    def validate_password (self, value):
        if value != 'sumbayak611':
            raise LazyAPIView.Error (('password', "Wrong password."))
        return value


class UploadSerializer (ViewSerializer):
    uri = AlphaNumericField (required=False)
    file = rfserializer.FileField ()
    
    def validate_uri (self, value: str):
        try:
            print (value)
            Code.objects.get (uri=value)
            raise LazyAPIView.Error (('uri', 'URL already taken'))
        except Code.DoesNotExist:
            print (value)
            try:
                Reserved.objects.get (word=value)
                print (value)
                raise LazyAPIView.Error (
                    ('uri', 'Sorry, this URL has been reserved for internal use (:.'))
            except Reserved.DoesNotExist:
                print (value)
                return value
    
    def validate_file (self, value: InMemoryUploadedFile):
        if value.size > 2 * 1000 * 1000:  # 10MB
            raise LazyAPIView.Error (('file', 'Max uploaded file size is 10 Mb.'))
        return value


class UpdateSerializer (URISerializer):
    version = rfserializer.IntegerField ()
    patches = rfserializer.JSONField (required = False)
    language = rfserializer.IntegerField (required = False)

    def validate_language (self, value):
        try:
            Language.objects.get (id = value)
            return value
        except Language.DoesNotExist:
            raise LazyAPIView.Error (('language', 'Language does not exists.'), 404)
    
    def validate_version (self, value):
        if self.validation_result.version != value:
            raise LazyAPIView.Error (('version', 'Version does not match.'))
        return value
