from django.urls import path, re_path, include

from . import views

urlpatterns = [
    path ('', views.New.as_view (), name = 'new'),
    path ('upload', views.Upload.as_view (), name = 'upload'),
    re_path ('^(?P<uri>[0-9A-Za-z]+$)', views.Open.as_view (), name = 'open'),
    re_path ('^(?P<uri>[0-9A-Za-z]+)/', include ('web.code.urls'))
    # re_path ('(?:^(?P<code>[0-9A-Za-z]+$))?$', views.index),
]
