from django.http.response import HttpResponseBase
from django.shortcuts import render
from django.views import View
from rest_framework import serializers, exceptions
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Code


class Lazy (object):
    """
    A base class that helps trim request handling processes with the same pattern.
    """
    request = None
    headers = None
    args = None
    kwargs = None
    user = None
    data = {}
    response = None
    methods = None
    
    def validate (self):
        """
        validate request data. If HttpResponseBase returned here, it will be given as response and
        http-method specific method will not be called. If it returned True, it will skip http_method
        specific handler and call default response (respond() method) instead.
        
        :return: early validation response or condition if request is not valid
        :rtype: Union[HttpResponseBase, boolean]
        """
        pass
    
    def handler_not_provided (self):
        """
        :return: not method-specific method defined. Check for its method availability to decide
                 whether it should call self.respond() method or not.
        :rtype: HttpResponseBase
        """
        if self.methods is None or self.methods != '__all__' and isinstance (self.methods, (list, tuple)) and self.request.method.lower () not in self.methods:
            raise MethodNotAllowed (self.request.method)
    
    def respond (self):
        """
        :return: response to be given as default for every http request.
                 It will overwrite any http response returned by http_method specific handler.
        :rtype: HttpResponseBase
        """
        pass
    
    def dispatch (self, request, *args, **kwargs):
        """
        entry point for every request.
        
        :param request:
        :type request:
        :return: response for request
        :rtype: HttpResponseBase
        """
        pass
    
    def add_data (self, key, value=None):
        """
        add data to be passed to context
        
        :param key: can be a key to access this value later on,
                    dict to be appended to current context, or
                    key-value value pair in form of tuple or list.
        :type key: Union[str, dict, tuple, list]
        :param value: value
        :type value: Any
        :return: nothing
        :rtype: None
        """
        if value:
            self.data[key] = value
        elif isinstance (key, dict):
            self.data.update (key)
        elif isinstance (key, (tuple, list)):
            for k, v in key:
                self.data[k] = v
    
    class Error (Exception):
        """
        base class for Error that should be caught by this view. It should handle error by itself.
        """
        def handle (self, view):
            """
            If return something, it will be treated as early response. You can raise another
            exception here to forward it to django's top level exception cather.
            
            :param view: view this exception was caught at
            :type view: Lazy
            :return: response or nothing
            :rtype: Union[HttpResponseBase, None]
            """
            raise NotImplementedError ('Every Exception derived from LazyView.Error must implements its own exception handling')


class LazyView (Lazy, View):
    def dispatch (self, request, *args, **kwargs):
        self.request = request
        self.args = args
        self.kwargs = kwargs
        
        if request.user.is_authenticated:
            ''' set self.user only if it is authenticated to avoid AnonymousUser '''
            self.user = request.user
        
        try:
            validation = self.validate ()
        except LazyView.Error as exception:
            validation = exception.handle (self)
        
        if isinstance (validation, HttpResponseBase):
            ''' validate() method returned something to be handled as response '''
            return validation
        
        '''
        get handler method.
        check if http_method specific handler exists.
        call for handler_not_provided otherwise
        '''
        handler = getattr (self, request.method.lower (), self.handler_not_provided)
        
        ''' call handler() if request valid. either way call respond(). '''
        return (not validation and handler ()) or self.respond ()


class LazyRenderView (LazyView):
    """ Skeleton for view that do simple render process """
    
    # template used for GET method
    _template_name = None
    
    # template used for post business logic (POST method)
    _post_template_name = None
    
    @property
    def post_template_name (self):
        """
        :return: template used for POST method only if current request method is POST
        :rtype: Union[str, None]
        """
        if self.request.method == 'post':
            return self.post_template_name
    
    @property
    def template_name (self):
        """
        check for POST template existence first.
        use GET template if no POST template exists.
        or simply use lowercase of view name as template name.
        
        :return: template name should be used under current circumstances.
        :rtype: str
        """
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
        """
        render template along with self.data as context.
        
        :return: render of self.template_name along with self.data as context
        :rtype: HttpResponse
        """
        return render (self.request, self.template_name, self.data)
    
    def respond (self):
        """
        default response for each RenderView will simply render template without any processing.
        
        :return: early render of self.template_name
        :rtype: HttpResponse
        """
        return self.render ()


class LazyAPIView (Lazy, APIView):
    """
    base view for view that shorten APIView pattern. It automatically wrap data with serializer
    specified for the class, validate data, and pass the data validation as context data.
    """
    
    # final input data
    __input = None
    
    # final output data.
    __output = None
    
    # serializer class specified to handle both input and output
    _serializer_class = None
    
    # serializer class specified to handle input
    _serializer_class_in = None
    
    # serializer class specified to handle output
    _serializer_class_out = None
    
    @property
    def input (self):
        return self.__input
    
    @property
    def output (self):
        return self.__output
    
    def get_output (self):
        """
        input_serializer can set an attribute named validation_result to be treated as output
        for this view and will be used as input for specified output_serializer.
        
        Method-specific handler can set the output to be processed automatically
        by output_serializer, if specified, with self.output() method and will take
        precedence over input_serializer.validation_result.
        
        :return: output to be returned as validation result
        :rtype: Union[serializers.SerializerMetaClass, Any]
        """
        return self.output or self.input.validation_result
    
    def set_output (self, output):
        self.__output = output
    
    @property
    def serializer_class (self):
        """
        :return: serializer class for both input and output data if specified.
        :rtype: serializers.SerializerMetaClass
        """
        return getattr (self.__class__, 'Serializer', self._serializer_class)
    
    @property
    def input_serializer (self):
        """
        Simply check for self._serializer_class_in attribute. But use inner class named
        InputSerializer first if exists.
        
        :return: serializer class for input data if specified.
        :rtype: serializers.SerializerMetaClass
        """
        input = getattr (self.__class__, 'InputSerializer', self._serializer_class_in)
        if not (self.serializer_class or input):
            raise LazyAPIView.SerializerNotSet ('input')
        return self.serializer_class or input
    
    @property
    def output_serializer (self):
        """
        Simply check for self._serializer_class_out attribute. But use inner class named
        OutputSerializer first if exists.

        :return: serializer class for output data if specified.
        :rtype: serializers.SerializerMetaClass
        """
        output = getattr (self.__class__, 'OutputSerializer', self._serializer_class_out)
        if not (self.serializer_class or output):
            raise LazyAPIView.SerializerNotSet ('output')
        return self.serializer_class or output
    
    def validate (self):
        """
        validate data using serializer returned by self.input_serializer
        """
        data = self.request.data or self.request.query_params or {}
        input = self.input_serializer (data=data)
        input.is_valid (raise_exception=True)
        self.__input = input
    
    def respond (self):
        """
        :return: response to be used as default for each APIView request
        :rtype: Response
        """
        output = self.output_serializer (self.get_output ())
        return Response (output.data)
    
    def get_response (self):
        """
        same as dispatch function for LazyView.
        
        :return: response
        :rtype: HttpResponseBase
        """
        try:
            validation = self.validate ()
        except LazyAPIView.Error as exc:
            validation = exc.handle (self)
        
        if isinstance (validation, HttpResponseBase):
            return validation
        
        try:
            handler = getattr (self, self.request.method.lower (), self.handler_not_provided)
            return (not validation and handler ()) or self.respond ()
        except LazyAPIView.Error as exc:
            return exc.handle (self)
    
    def dispatch (self, request, *args, **kwargs):
        """
        override dispatch method of APIView with some tweak to match LazyView pattern.
        
        :param request: request object
        :type request: rest_framework.request.Request
        :return: response for request
        :rtype: HttpResponseBase
        """
        request = self.initialize_request (request, *args, **kwargs)
        self.request = request
        self.args = args
        self.kwargs = kwargs
        self.headers = self.default_response_headers
        print (request.data)
        
        if request.user.is_authenticated:
            ''' set self.user only if it is authenticated to avoid AnonymousUser '''
            self.user = request.user
    
        try:
            self.initial (request, *args, **kwargs)
            response = self.get_response ()
        except Exception as exc:
            response = self.handle_exception (exc)
    
        self.response = self.finalize_response (request, response, *args, **kwargs)
        return self.response
    
    class Error (Lazy.Error):
        """
        Error class for API views. It receives details to be returned as value for json object
        named 'details'. Every exceptions will simply return json with this format:
        
        { 'details': self.details }
        """
        
        # exception details or info
        details = None
        status = None
        code = None
        
        def __init__ (self, details, status=None, code=None):
            """
            :param details: details of information to be displayed about this exception
            :type details: Union[str, tuple, list, dict]
            :param status: HTTP status code
            :type status: int
            :param code: Error code to distinguish the problem/cause
            :type code: str
            """
            self.details = details
            self.status = status
            self.code = code
        
        def handle (self, view):
            """
            use serializers.ValidationError to forward exception to Django Rest Framework exception
            cather which render exception as json response.
            If return something, it will be treated as early response.
            
            :param view: view this exception was caught at.
            :type view: LazyAPIView
            :return: response
            :rtype: HttpResponseBase
            """
            if isinstance (self.details, dict):
                detail = self.details
            elif isinstance (self.details, tuple):
                detail = {self.details[0]: self.details[1]}
            else:
                detail = {'details': self.details}
            
            if self.status == 404:
                exc = exceptions.NotFound
            else:
                exc = exceptions.ValidationError
            raise exc (detail, self.code)
    
    class SerializerNotSet (Error):
        def __init__ (self, type):
            super ().__init__ ('Serializer (%s) is not set' % type)


class URIView (LazyView):
    """
    class that pre-process uri-related views. It extract uri string from request url or
    request data, and do some validations on it.
    """
    
    # uri for current request
    uri = None
    
    def uri_not_set (self):
        """
        uri not found on either request url nor request data.
        Raise Lazy.
        
        :return: str to be given as new uri if uri not set
        :rtype: str
        """
        pass
    
    def extract_uri (self):
        uri = self.request.POST.get ('uri') or self.kwargs.get ('uri')
        if not uri:
            uri = self.uri_not_set ()
        return uri
    
    def validate (self):
        super ().validate ()
        self.uri = self.extract_uri ()
    
    class LengthExceeded (Lazy.Error):
        def handle (self, view):
            return view.uri_length_exceeded ()


class CodeView (URIView):
    """ View that retrieve a Code object to be processed later on. """
    
    # code for current request
    code = None
    
    def code_does_not_exist (self):
        """
        code with given uri does not exists in database.
        
        :return: response to be given if code does not exists
        :rtype: Code
        """
        pass
    
    def code_not_authorized (self):
        """
        The request being handled is not authorized to access this code.
        This method will be called at dispatch level.
        
        :return: response in this case
        :rtype: HttpResponseBase
        """
        pass
    
    def extract_code (self):
        try:
            return Code.objects.get (uri=self.uri)
        except Code.DoesNotExist:
            _ = Code.objects.get (uri='_')
            return self.code_does_not_exist () or _
    
    def validate (self):
        super ().validate ()
        self.code = self.extract_code ()
        self.add_data ('code', self.code)
        if self.code.is_password_protected () and not self.request.session.get (self.code.uri):
            raise CodeView.NotAuthorized ()
    
    class DoesNotExist (Lazy.Error):
        def handle (self, view):
            return view.code_does_not_exist ()
    
    class NotAuthorized (Lazy.Error):
        def handle (self, view):
            return view.code_not_authorized ()
