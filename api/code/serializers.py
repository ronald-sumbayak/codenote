from rest_framework import serializers

from core.models import Code, Reserved
from core.serializers import URISerializer, AlphaNumericField
from core.views import LazyAPIView


class CheckURISerializer (URISerializer):
    def validate_uri (self, value):
        try:
            print (super ().validate_uri (value))
        except LazyAPIView.Error as err:
            print (err)
            if err.status == 404:
                return value
            raise err
        raise LazyAPIView.Error (('uri', 'URL has already been used'))


class PasswordSerializer (URISerializer):
    password = serializers.CharField (trim_whitespace=False)


class RenameSerializer (URISerializer):
    new_uri = AlphaNumericField ()
    
    def validate_new_uri (self, value):
        try:
            Code.objects.get (uri=value)
            raise LazyAPIView.Error (('new_uri', 'URL already taken'))
        except Code.DoesNotExist:
            try:
                Reserved.objects.get (word=value)
                raise LazyAPIView.Error (
                    ('new_uri', 'Sorry, this URL has been reserved for internal use (:'))
            except Reserved.DoesNotExist:
                return value
