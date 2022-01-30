from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'articles'


urlpatterns = [
    url(r'^$', views.homepage, name="list"),
    url(r'^contact/$', views.contact, name="contact"),
    url(r'^classAndSubjects/$', views.classAndSubjects, name="classAndSubjects"),
    url(r'^canvas/$', views.Canvas, name="canvas"),


]
