from django.http import HttpResponse
from django.shortcuts import redirect

from core.views import CodeView, LazyView
from web.views import LazyRenderView


class Highlight (CodeView, LazyRenderView):
    pass


class Raw (CodeView, LazyView):
    def get (self):
        return HttpResponse (self.code.source.encode (), content_type = 'text/plain')


class Download (CodeView, LazyView):
    def get (self):
        response = HttpResponse (self.code.source.encode (), content_type = 'text/plain')
        response['Content-Disposition'] = 'attachment; filename=%s.codenote' % self.uri
        return response


class Locked (CodeView, LazyRenderView):
    def code_not_authorized (self):
        print ('cok')
        return True
    
    def get (self):
        print ('uri')
        return redirect ('/' + self.uri)
