from django.conf.urls import url
from django.urls import path

from . import views


app_name = 'articles'


urlpatterns = [
    url(r'^$', views.homepage, name="list"),
    url(r'^contact/$', views.contact, name="contact"),
    url(r'^classAndSubjects/$', views.classAndSubjects, name="classAndSubjects"),
    url(r'^canvas/$', views.Canvas, name="canvas"),
    url(r'^questions/$', views.questionsss, name="questions"),
    url(r'^questionsGenerate/$', views.questionsGenerate, name="questionsGenerate"),
    path('removequestion/<str:pk>/$', views.removequestion, name="removequestion"),
    path('editquestion/<str:pk>/$', views.editquestion, name="editquestion"),
    path('addquestion/<str:pk>/$', views.addquestion, name="addquestion"),
    path('addquestionSelective/<str:pk>/$', views.addquestionSelective, name="addquestionSelective"),
    url(r'^questioninput/$', views.questioninput, name="questioninput"),
    url(r'^bijoyinput/$', views.bijoyinput, name="bijoyinput"),
    url(r'^unicodeinput/$', views.unicodeinput, name="unicodeinput"),
    url(r'^unicodeinputSelective/$', views.unicodeinputSelective, name="unicodeinputSelective"),
    url(r'^bijoyinputSelective/$', views.bijoyinputSelective, name="bijoyinputSelective"),
]
