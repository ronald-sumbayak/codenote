from django.urls import path

from . import views

urlpatterns = [
    path ('refresh_compilers', views.RefreshCompilerList.as_view (), name='refresh_compilers'),
    path ('rename', views.Rename.as_view (), name='rename'),
    path ('lock', views.Lock.as_view (), name='lock'),
    path ('unlock', views.Unlock.as_view (), name='unlock'),
    path ('check_password', views.CheckPassword.as_view (), name='check_password'),
    path ('update', views.Update.as_view (), name='update'),
    path ('compile', views.Compile.as_view (), name='compile'),
    path ('check_submission', views.CheckSubmission.as_view (), name='check_submission'),
]
