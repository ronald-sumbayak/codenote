from django.urls import path

from . import views

urlpatterns = [
    path ('code', views.Highlight.as_view (), name = 'code'),
    path ('raw', views.Raw.as_view (), name = 'raw'),
    path ('download', views.Download.as_view (), name = 'download'),
    path ('locked', views.Locked.as_view (), name = 'locked')
]
