from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models


class Compiler (models.Model):
    id = models.IntegerField (
        'Compiler ID',
        primary_key = True,
        help_text = 'compiler id')
    name = models.CharField (
        'Compiler Name',
        max_length = 128,
        help_text = 'compiler name')
    ver = models.CharField (
        'Compiler Version',
        max_length = 128,
        help_text = 'compiler version')
    short = models.CharField (
        'Compiler Short Name',
        max_length = 128,
        help_text = 'short name')
    ace = models.CharField (
        'Ace',
        max_length = 128,
        blank = True,
        help_text = 'syntax highlighting identifier for Ace')
    geshi = models.CharField (
        'Geshi',
        max_length = 128,
        blank = True,
        help_text = 'syntax highlighting identifier for Geshi')
    pygments = models.CharField (
        'Pygments',
        max_length = 128,
        blank = True,
        help_text = 'syntax highlighting identifier for Pygments')
    highlights = models.CharField (
        'Highlights',
        max_length = 128,
        blank = True,
        help_text = 'syntax highlighting identifier for Highlights')
    rouge = models.CharField (
        'Rouge',
        max_length = 128,
        blank = True,
        help_text = 'syntax highlighting identifier for Rouge')
    codemirror = models.CharField (
        'CodeMirror',
        max_length = 128,
        blank = True,
        help_text = 'syntax highlighting identifier for CodeMirror')
    
    def __str__ (self):
        return self.name
    
    class Meta:
        ordering = ['id']


class Submission (models.Model):
    STATUS_WAITING = -1
    STATUS_FINISHED = 0
    STATUS_COMPILATION = 1
    STATUS_RUNNING = 3
    STATUS_CHOICES = [
        (STATUS_FINISHED, 'Finished'),
        (STATUS_COMPILATION, 'Compilation'),
        (STATUS_RUNNING, 'Running'),
        (STATUS_WAITING, 'Waiting For Compilation')]
    
    RESULT_COMPILATION_ERROR = 11
    RESULT_RUNTIME_ERROR = 12
    RESULT_TIME_LIMIT_EXCEEDED = 13
    RESULT_SUCCESS = 15
    RESULT_MEMORY_LIMIT_EXCEEDED = 17
    RESULT_ILLEGAL_SYSTEM_CALL = 19
    RESULT_INTERNAL_ERROR = 20
    RESULT_CHOICES = [
        (RESULT_COMPILATION_ERROR, 'Compilation Error'),
        (RESULT_RUNTIME_ERROR, 'Runtime Error'),
        (RESULT_TIME_LIMIT_EXCEEDED, 'Time Limit Exceeded'),
        (RESULT_SUCCESS, 'Success'),
        (RESULT_MEMORY_LIMIT_EXCEEDED, 'Memory Limit Exceeded'),
        (RESULT_ILLEGAL_SYSTEM_CALL, 'Illegal System Call'),
        (RESULT_INTERNAL_ERROR, 'Internal Error')]
    
    id = models.IntegerField (
        'Submission ID',
        primary_key = True,
        help_text = 'id of created submission')
    source = models.TextField (
        'Source',
        blank = True,
        null = True,
        help_text = 'source code to run, default: empty')
    compiler = models.ForeignKey (
        Compiler,
        models.SET_NULL,
        blank = True,
        null = True,
        default = 1,
        help_text = 'compiler identifier, default: 1 (C++)')
    input = models.TextField (
        'Input',
        blank = True,
        null = True,
        help_text = 'data that will be provided to the program as stdin stream, default: empty')
    time = models.FloatField (
        'Execution Time',
        help_text = 'execution time in seconds',
        validators = [MinValueValidator (0.0)])
    memory = models.IntegerField (
        'Memory Consumed',
        help_text = 'memory consumed by the program in kilobytes')
    date = models.DateTimeField (
        'Creation DateTime',
        help_text = 'creation date and time (on server);\n'
                    'format: yyyy-mm-­dd hh:mm:ss; eg. 2009­-05-­19 02:­34:­56')
    status = models.IntegerField (
        'Status',
        choices = STATUS_CHOICES,
        help_text = 'current status; see section "Status and result"')
    result = models.IntegerField (
        'Result',
        choices = RESULT_CHOICES,
        help_text = 'current result; see section "Status and result"')
    signal = models.IntegerField (
        'Signal',
        help_text = 'signal raised by the program')
    
    def __str__ (self):
        return str (self.id)


class Code (models.Model):
    owner = models.ForeignKey (
        User,
        models.SET_NULL,
        blank = True,
        null = True,
        verbose_name = 'Owner/Creator',
        help_text = 'the user logged in at the time this code/note created')
    uri = models.SlugField (
        'URI',
        max_length = 64,
        unique = True,
        help_text = 'URI identifier for this code, randomly generated if not set')
    source = models.TextField (
        'Source',
        blank = True,
        null = True,
        default = '',
        help_text = 'last captured version')
    password = models.CharField (
        'Password',
        max_length = 128,
        blank = True,
        null = True,
        help_text = 'password, if any')
    version = models.IntegerField (
        'Version',
        default = 0,
        help_text = 'version counter')
    last_submission = models.ForeignKey (
        Submission,
        models.SET_NULL,
        blank = True,
        null = True,
        help_text = 'last code submission')
    
    def is_password_protected (self):
        return self.password is not None
    
    def set_password (self, raw_password):
        self.password = make_password (raw_password)
    
    def check_password (self, raw_password):
        def setter (raw_password):
            self.set_password (raw_password)
            self.save (update_fields = ['password'])
        return check_password (raw_password, self.password, setter)
    
    def remove_password (self):
        self.password = None
    
    def commit (self, source, version):
        if self.version == version:
            self.source = source
            self.version += 1
    
    @property
    def data (self):
        return {
            'owner': self.owner_id,
            'code': self.uri,
            'source': self.source.encode (),
            'password_protected': self.password is not None,
            'version': self.version,
            'last_submission': self.last_submission_id}
    
    def __str__ (self):
        return self.uri


class Reserved (models.Model):
    word = models.CharField (max_length = 64)
    
    def __str__ (self):
        return self.word
