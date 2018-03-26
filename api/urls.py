from django.urls import path

from . import views
from .code import views as code_views
from .common import views as common_views

urlpatterns = [
    path ('refresh', common_views.RefreshCompiler.as_view (), name= 'refresh'),
    path ('upload', common_views.Upload.as_view (), name='upload-api'),
    path ('update', common_views.Update.as_view (), name='update'),
    
    path ('code', code_views.RetrieveCode.as_view (), name='code'),
    path ('check', code_views.Check.as_view (), name='check'),
    path ('rename', code_views.Rename.as_view (), name='rename'),
    path ('lock', code_views.Lock.as_view (), name='lock'),
    path ('unlock', code_views.Unlock.as_view (), name='unlock'),
    path ('password', code_views.CheckPassword.as_view (), name='password'),
    
    path ('compile', views.Compile.as_view (), name='compile'),
    path ('submission', views.CheckSubmission.as_view (), name='submission'),
]
