from django.contrib import admin

from .models import Language, Submission, Code, Reserved

admin.site.register ([
    Submission,
    Code,
    Reserved])


@admin.register (Language)
class CompilerAdmin (admin.ModelAdmin):
    list_display = ['name', 'id', 'mime', 'highlights', 'codemirror']
