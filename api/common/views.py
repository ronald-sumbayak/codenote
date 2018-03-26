from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from sphere_engine import CompilersClientV3

from codenote.settings import COMPILERS_API_ENDPOINT, COMPILERS_API_TOKEN
from core.models import Code, Language, generate_random_uri
from core.serializers import CodeSerializer
from core.views import LazyAPIView
from . import serializers


class RefreshCompiler (LazyAPIView):
    authentication_classes = [SessionAuthentication]
    _serializer_class_in = serializers.RefreshSerializer
    
    def post (self):
        client = CompilersClientV3 (COMPILERS_API_TOKEN, COMPILERS_API_ENDPOINT)
        result: dict = client.compilers ()
        if result.get ('error') == 'OK':
            for c in result.get ('items'):
                for key in c:
                    try:
                        if len (c.get (key)) == 0:
                            c[key] = None
                    except TypeError:
                        pass
                compiler, created = Language.objects.get_or_create (id = c.get ('id'), defaults = c)
                if not created:
                    for key, value in c.items ():
                        setattr (compiler, key, value)
                    compiler.save ()
            return Response (result)
        else:
            raise LazyAPIView.Error ('Failed to retrieve compiler List')


class Upload (LazyAPIView):
    _serializer_class_in = serializers.UploadSerializer
    _serializer_class_out = CodeSerializer
    
    def post (self):
        uri = self.input.validated_data.get ('uri') or generate_random_uri ()
        file = self.input.validated_data.get ('file')
        code = Code.objects.create (uri=uri, source=file.read ())
        self.set_output (code)


class Update (LazyAPIView):
    _serializer_class_in = serializers.UpdateSerializer
    _serializer_class_out = CodeSerializer
    
    def post (self):
        code = self.input.validation_result
        
        if 'patches' in self.input.validated_data:
            for change in self.input.validated_data['patches']:
                try:
                    change_type, i, j = change
                    if change_type == 1:
                        text = j
                        code.source = code.source[:i] + text + code.source[i:]
                    else:
                        length = j
                        code.source = code.source[:i] + code.source[i + length:]
                except:
                    raise LazyAPIView.Error (('patches', 'Patches is not valid.'))
        
        if 'language' in self.input.validated_data:
            code.language_id = self.input.validated_data['language']
        
        self.set_output (code.save ())
    
