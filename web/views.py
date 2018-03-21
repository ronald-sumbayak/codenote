import exrex
from django.shortcuts import redirect

from core.models import Code, Compiler
from core.views import CodeView, LazyView, LazyRenderView


def generate_random_uri ():
    """
    Generate random URI that has not been used.
    
    :return: uri
    :rtype: str
    """
    while True:
        uri = exrex.getone ('[0-9A-Za-z]{6}')
        try:
            Code.objects.get (uri=uri)
        except Code.DoesNotExist:
            return uri


class New (LazyView):
    def get (self):
        return redirect ('open', generate_random_uri ())


class Upload (LazyRenderView):
    pass


class Open (CodeView, LazyRenderView):
    def code_does_not_exist (self):
        return Code.objects.create (owner=self.user, uri=self.uri)
    
    def get (self):
        self.add_data ('compilers', Compiler.objects.filter (codemirror__isnull=False, mime__isnull=False))
