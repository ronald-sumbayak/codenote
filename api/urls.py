from django.urls import path

from . import views

urlpatterns = [
    path ('compilers/refresh', views.refresh_compilers_list, name = 'refresh_compilers'),
    path ('rename', views.Rename.as_view (), name = 'rename'),
    path ('lock', views.Lock.as_view (), name = 'lock'),
    path ('unlock', views.Unlock.as_view (), name = 'unlock'),
    path ('update', views.Update.as_view (), name = 'update'),
    path ('compile', views.Compile.as_view (), name = 'compile'),
    path ('check', views.Check.as_view (), name = 'check')
]
