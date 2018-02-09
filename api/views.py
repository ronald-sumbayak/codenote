from pprint import pprint

from django.http import JsonResponse
from django.utils.translation import ugettext_lazy
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from sphere_engine import CompilersClientV3

from codenote.settings import COMPILERS_API_ENDPOINT, COMPILERS_API_TOKEN
from core.models import Code, Compiler
from core.serializers import CodeSerializer
from core.views import CodeView, RenderView


def refresh_compilers_list (request):
    client = CompilersClientV3 (COMPILERS_API_TOKEN, COMPILERS_API_ENDPOINT)
    print (client.api_client)
    compilers = client.compilers ()
    for c in compilers['items']:
        compiler = Compiler.objects.filter (id = c.get ('id', ))
        print (c.get ('id', ))
        pprint (compiler, indent = 4)
        compiler.update_or_create (defaults = c)
    return JsonResponse (compilers)


class Lock (APIView):
    class Serializer (serializers.Serializer):
        uri = serializers.SlugField ()
        password = serializers.CharField (trim_whitespace = False)
        
        def update (self, instance, validated_data):
            pass
        
        def create (self, validated_data):
            pass
        
        def validate (self, attrs):
            uri = attrs.get ('uri')
            password = attrs.get ('password')
            if uri and password:
                try:
                    attrs['code'] = Code.objects.get (uri = uri)
                    return attrs
                except Code.DoesNotExist:
                    raise serializers.ValidationError (ugettext_lazy ('Code Does Not Exists'))
            else:
                raise serializers.ValidationError (ugettext_lazy ('Must include "uri" and "password"'))
    
    def post (self):
        serializer = Lock.Serializer (data = self.request.data)
        serializer.is_valid (raise_exception = True)
        code = serializer.validated_data.get ('code')
        code.set_password (serializer.validated_data.get ('password'))
        code.save ()
        return Response (CodeSerializer (code).data)


class Unlock (CodeView, RenderView):
    class Serializer (serializers.Serializer):
        uri = serializers.SlugField ()
        
        def update (self, instance, validated_data):
            pass
        
        def create (self, validated_data):
            pass
        
        def validate (self, attrs):
            uri = attrs.get ('uri')
            if uri:
                try:
                    attrs['code'] = Code.objects.get (uri = uri)
                    return attrs
                except Code.DoesNotExist:
                    raise serializers.ValidationError (ugettext_lazy ('Code Does Not Exists'))
            else:
                raise serializers.ValidationError (ugettext_lazy ('Must include "uri"'))
                
    def post (self):
        serializer = Unlock.Serializer (data = self.request.data)
        serializer.is_valid (raise_exception = True)
        code = serializer.validated_data.get ('code')
        code.password = None
        code.save ()
        return Response (CodeSerializer (code).data)


class Rename (CodeView, APIView):
    class Serializer (serializers.Serializer):
        uri = serializers.SlugField ()
        new_uri = serializers.SlugField ()

        def update (self, instance, validated_data):
            pass

        def create (self, validated_data):
            pass

        def validate (self, attrs):
            uri = attrs.get ('uri')
            new_uri = attrs.get ('new_uri')
            if uri and new_uri:
                try:
                    attrs['code'] = Code.objects.get (uri = uri)
                except Code.DoesNotExist:
                    raise serializers.ValidationError (ugettext_lazy ('Code does not exists'))
                
                try:
                    Code.objects.get (uri = new_uri)
                    raise serializers.ValidationError (ugettext_lazy ('URI already used'))
                except Code.DoesNotExist:
                    return attrs
            else:
                raise serializers.ValidationError (ugettext_lazy ('Must include "uri" and "new_uri"'))
    
    def post (self):
        serializer = Rename.Serializer (data = self.request.data)
        serializer.is_valid (raise_exception = True)
        code = serializer.validated_data.get ('code')
        code.uri = serializer.validated_data.get ('new_uri')
        code.save ()
        return Response (CodeSerializer (code).data)


class Compile (RenderView):
    pass


class Check (RenderView):
    pass


class Update (RenderView):
    pass
