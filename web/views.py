from django.shortcuts import redirect

from core.models import Code, Language, generate_random_uri
from core.views import CodeView, LazyRenderView, LazyView


class New (LazyView):
    def get (self):
        return redirect ('open', generate_random_uri ())


class Upload (LazyRenderView):
    methods = ['get']


class Open (CodeView, LazyRenderView):
    def code_does_not_exist (self):
        return Code.objects.create (owner=self.user, uri=self.uri)
    
    def get (self):
        self.add_data ('languages', Language.objects.filter (codemirror__isnull=False, mime__isnull=False))
