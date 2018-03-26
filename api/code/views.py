from rest_framework.response import Response

from core.serializers import CodeSerializer, URISerializer
from core.views import CodeView, LazyAPIView
from . import serializers


class RetrieveCode (LazyAPIView, CodeView):
    _serializer_class_in = URISerializer
    _serializer_class_out = CodeSerializer
    methods = ['post']


class Check (LazyAPIView):
    _serializer_class_in = serializers.CheckURISerializer
    methods = ['post']
    
    def post (self):
        return Response ({'uri': 'Available'})


class Lock (LazyAPIView):
    _serializer_class_in = serializers.PasswordSerializer
    _serializer_class_out = CodeSerializer
    
    def post (self):
        code = self.input.validation_result
        code.set_password (self.input.validated_data.get ('password'))
        self.set_output (code.save ())


class CheckPassword (LazyAPIView):
    _serializer_class_in = serializers.PasswordSerializer
    _serializer_class_out = CodeSerializer
    
    def post (self):
        code = self.input.validation_result
        if not code.check_password (self.input.validated_data.get ('password')):
            raise LazyAPIView.Error (('password', 'Wrong Password'))
        self.set_output (code)


class Unlock (LazyAPIView):
    _serializer_class_in = URISerializer
    _serializer_class_out = CodeSerializer
    
    def post (self):
        code = self.input.validation_result
        code.password = None
        self.set_output (code.save ())


class Rename (LazyAPIView):
    _serializer_class_in = serializers.RenameSerializer
    _serializer_class_out = CodeSerializer
    
    def post (self):
        code = self.input.validation_result
        code.uri = self.input.validated_data.get ('new_uri')
        self.set_output (code.save ())
