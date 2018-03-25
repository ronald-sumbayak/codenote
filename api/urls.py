from django.urls import path

from . import views

urlpatterns = [
    path ('refresh', views.RefreshCompiler.as_view (), name= 'refresh'),
    path ('code', views.RetrieveCode.as_view (), name='code'),
    path ('check', views.Check.as_view (), name='check'),
    path ('upload', views.Upload.as_view (), name='upload-api'),
    path ('rename', views.Rename.as_view (), name='rename'),
    path ('lock', views.Lock.as_view (), name='lock'),
    path ('unlock', views.Unlock.as_view (), name='unlock'),
    path ('password', views.CheckPassword.as_view (), name='password'),
    path ('update', views.Update.as_view (), name='update'),
    path ('compile', views.Compile.as_view (), name='compile'),
    path ('submission', views.CheckSubmission.as_view (), name='submission'),
]
