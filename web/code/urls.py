from django.urls import path

from . import views

urlpatterns = [
    path ('share', views.Raw.as_view (), name='share'),
    path ('raw', views.Raw.as_view (), name='raw'),
    path ('highlight', views.Highlight.as_view (), name='highlight'),
    path ('download', views.Download.as_view (), name='download'),
    path ('locked', views.Locked.as_view (), name='locked')
]
