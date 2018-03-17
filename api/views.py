from pprint import pprint

from django.http import JsonResponse
from rest_framework import serializers
from rest_framework.response import Response
from sphere_engine import CompilersClientV3

from codenote.settings import COMPILERS_API_ENDPOINT, COMPILERS_API_TOKEN
from core.models import Code, Compiler
from core.serializers import CodeSerializer, URISerializer, CompilerSerializer
from core.views import LazyAPIView, LazyRenderView


class RefreshCompilerList (LazyAPIView):
    def validate (self):
        pass
    
    def post (self):
        client = CompilersClientV3 (COMPILERS_API_TOKEN, COMPILERS_API_ENDPOINT)
        result: dict = client.compilers ()
        if result.get ('error') == 'OK':
            for c in result.get ('items'):
                compiler = Compiler.objects.filter (id = c.get ('id'))
                compiler.update_or_create (defaults = c)
            return Response (result)
        else:
            raise LazyAPIView.Error ('Failed to retrieve compiler List')


def refresh_compilers (request):
    client = CompilersClientV3 (COMPILERS_API_TOKEN, COMPILERS_API_ENDPOINT)
    print (client.api_client)
    compilers: dict = client.compilers ()
    for c in compilers['items']:
        compiler = Compiler.objects.filter (id = c.get ('id'))
        print (c.get ('id'))
        pprint (compiler, indent = 4)
        compiler.update_or_create (defaults = c)
    return JsonResponse (compilers)


class Lock (LazyAPIView):
    _serializer_class_out = CodeSerializer
    
    def post (self):
        code = self.input.validation_result
        code.set_password (self.input.validated_data.get ('password'))
        code.save ()
        self.output = code
    
    class InputSerializer (URISerializer):
        password = serializers.CharField (trim_whitespace = False)


class CheckPassword (LazyAPIView):
    _serializer_class_out = CodeSerializer
    
    def post (self):
        code = self.input.validation_result
        if not code.check_password (self.input.validated_data.get ('password')):
            raise LazyAPIView.Error ('Wrong Password')
        self.output = code
    
    class InputSerializer (URISerializer):
        password = serializers.CharField (trim_whitespace = False)


class Unlock (LazyAPIView):
    _serializer_class_out = CodeSerializer
    
    def post (self):
        code = self.input.validation_result
        code.password = None
        code.save ()
        self.output = code
                
    class InputSerializer (URISerializer):
        pass


class Rename (LazyAPIView):
    _serializer_class_out = CodeSerializer
    
    def post (self):
        code = self.input.validation_result
        code.uri = self.input.validated_data.get ('new_uri')
        code.save ()
        self.output = code
    
    class InputSerializer (URISerializer):
        new_uri = serializers.SlugField ()
        
        def validate (self, attrs):
            super ().validate (attrs)
            try:
                Code.objects.get (uri = attrs.get ('new_uri'))
                raise LazyAPIView.Error ('URI already taken')
            except Code.DoesNotExist:
                return attrs


class Compile (LazyAPIView):
    pass


class CheckSubmission (LazyAPIView):
    pass


class Update (LazyAPIView):
    pass
