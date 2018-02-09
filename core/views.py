from django.http.response import HttpResponseBase
from django.shortcuts import render, redirect
from django.views import View

from .models import Code


class LazyView (View):
    request = None
    args = None
    kwargs = None
    user = None
    data = {}

    def validate (self):
        pass

    def handle (self):
        pass

    def handler_not_provided (self):
        pass

    def respond (self):
        pass

    def dispatch (self, request, *args, **kwargs):
        self.request = request
        self.args = args
        self.kwargs = kwargs
        if request.user.is_authenticated:
            self.user = request.user
        
        try:
            validation = self.validate ()
        except LazyView.Error as exception:
            validation = exception.handle (self)
        
        print (validation)
        if isinstance (validation, HttpResponseBase):
            return validation
        
        handler = getattr (self, request.method.lower (), self.handler_not_provided)
        return (not validation and handler ()) or self.respond ()
    
    def add_data (self, key, value=None):
        if value:
            self.data[key] = value
        elif isinstance (key, dict):
            self.data.update (key)
        elif isinstance (key, (tuple, list)):
            for k, v in key:
                self.data[k] = v
    
    class Error (Exception):
        def handle (self, view):
            raise NotImplementedError ('Every Exception derived from LazyView.Error must implements'
                                       'its own exception handling')


class RenderView (LazyView):
    _template_name = None
    _post_template_name = None
    
    @property
    def post_template_name (self):
        if self.request.method == 'post':
            return self.post_template_name
    
    @property
    def template_name (self):
        template_name = (
            self.post_template_name
            or
            self._template_name
            or
            self.__class__.__name__.lower ())
        if not template_name.lower ().endswith ('.html'):
            template_name += '.html'
        return template_name
    
    def render (self):
        return render (self.request, self.template_name, self.data)
    
    def respond (self):
        return self.render ()


class URIView (LazyView):
    uri = None
    
    def uri_not_set (self):
        pass
    
    def uri_length_exceeded (self):
        self._template_name = 'uri_length_exceeded'
        return True
    
    def extract_uri (self):
        uri = self.request.POST.get ('uri') or self.kwargs.get ('uri')
        if not uri:
            self.uri_not_set ()
        if len (uri) > 64:
            raise URIView.LengthExceeded ()
        return uri
    
    def validate (self):
        super ().validate ()
        self.uri = self.extract_uri ()
    
    class LengthExceeded (LazyView.Error):
        def handle (self, view):
            return view.uri_length_exceeded ()


class CodeView (URIView):
    code = None
    
    def code_does_not_exist (self):
        pass
    
    def code_not_authorized (self):
        # TODO: fix this redirect
        return redirect ('locked', self.uri)
    
    def extract_code (self):
        try:
            return Code.objects.get (uri = self.uri)
        except Code.DoesNotExist:
            _ = Code.objects.get (uri = '_')
            return self.code_does_not_exist () or _
    
    def validate (self):
        super ().validate ()
        self.code = self.extract_code ()
        self.add_data ('code', self.code)
        # TODO: check session
        if self.code.is_password_protected () and True: # check session
            raise CodeView.NotAuthorized ()
    
    class DoesNotExist (LazyView.Error):
        def handle (self, view):
            return view.code_does_not_exist ()
    
    class NotAuthorized (LazyView.Error):
        def handle (self, view):
            return view.code_not_authorized ()
