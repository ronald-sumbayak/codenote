from django.contrib import admin

from .models import Compiler, Submission, Code, Reserved

admin.site.register ([
    Submission,
    Code,
    Reserved])


@admin.register (Compiler)
class CompilerAdmin (admin.ModelAdmin):
    list_display = ['name', 'id', 'mime', 'highlights', 'codemirror']
