from django.contrib import admin

from .models import Compiler, Submission, Code, Reserved

admin.site.register ([
    Compiler,
    Submission,
    Code,
    Reserved])
