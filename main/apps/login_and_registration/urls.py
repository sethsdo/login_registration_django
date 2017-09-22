from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index), 
    url(r'^process$', views.register),
    url(r'^signIn$', views.signIn),
    url(r'^success$', views.success),
    url(r'^signOut$', views.signOut)
]
